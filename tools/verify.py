"""Check an install against the pinned images.

    uv run --frozen python tools/verify.py <install dir>

Each image in config/images.toml must be in the install with its size and SHA-256. Exits
non-zero on any failure. The symbol map's rules are x86port's tools/symbol_constants.py.
"""

import hashlib
import os
import sys
import tomllib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


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


def main(argv):
    if len(argv) != 2:
        sys.exit(__doc__)
    with open(os.path.join(ROOT, "config", "images.toml"), "rb") as file:
        images = tomllib.load(file)["image"]
    errors = []
    for image in images:
        errors += check_image(argv[1], image)
    for error in errors:
        print(error)
    print("%d image(s) checked, %d problem(s)" % (len(images), len(errors)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
