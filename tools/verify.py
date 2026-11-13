"""Check an install against the pinned images and the symbol map against those images.

    uv run --frozen python tools/verify.py <install dir>

Each image in config/images.toml must be in the install with its size and SHA-256. Every
symbol must lie inside a section of its image, a `type:func` or `type:label` one inside an
executable section, and no name or address may appear twice. Exits non-zero on any failure.
"""

import hashlib
import os
import re
import sys
import tomllib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYMBOL = re.compile(r"^(\w+)\s*=\s*0x([0-9A-Fa-f]+);\s*(?://\s*(.*))?$")


def check_image(install, image):
    path = os.path.join(install, image["file"])
    if not os.path.isfile(path):
        return ["%s: missing from %s" % (image["file"], install)]
    with open(path, "rb") as file:
        data = file.read()
    if len(data) != image["size"]:
        return ["%s: %d bytes, expected %d" % (image["file"], len(data), image["size"])]
    digest = hashlib.sha256(data).hexdigest()
    if digest != image["sha256"]:
        return ["%s: SHA-256 %s, expected %s" % (image["file"], digest, image["sha256"])]
    return []


def check_symbols(image):
    errors = []
    names = set()
    addresses = set()
    path = os.path.join(ROOT, image["symbols"])
    if not os.path.isfile(path):
        return [], 0
    count = 0
    with open(path) as file:
        for number, line in enumerate(file, 1):
            line = line.strip()
            if not line or line.startswith("//"):
                continue
            match = SYMBOL.match(line)
            where = "%s:%d" % (image["symbols"], number)
            if not match:
                errors.append("%s: not `name = 0xADDR; // type:...`" % where)
                continue
            name, address, comment = match.group(1), int(match.group(2), 16), match.group(3) or ""
            count += 1
            if name in names:
                errors.append("%s: %s named twice" % (where, name))
            if address in addresses:
                errors.append("%s: 0x%08X named twice" % (where, address))
            names.add(name)
            addresses.add(address)
            section = next((s for s in image["sections"]
                            if s["start"] <= address < s["start"] + s["size"]), None)
            if section is None:
                errors.append("%s: %s 0x%08X is in no section of %s" % (where, name, address, image["file"]))
            elif re.search(r"type:(func|label)", comment) and not section["execute"]:
                errors.append("%s: %s is code but 0x%08X is in %s" % (where, name, address, section["name"]))
    return errors, count


def main(argv):
    if len(argv) != 2:
        sys.exit(__doc__)
    with open(os.path.join(ROOT, "config", "images.toml"), "rb") as file:
        images = tomllib.load(file)["image"]
    errors = []
    symbols = 0
    for image in images:
        errors += check_image(argv[1], image)
        found, count = check_symbols(image)
        errors += found
        symbols += count
    for error in errors:
        print(error)
    print("%d image(s) checked, %d symbol(s) checked, %d problem(s)" % (len(images), symbols, len(errors)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
