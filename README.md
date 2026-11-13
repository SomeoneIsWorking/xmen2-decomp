# X-Men Legends II decomp

Reverse engineering of **X-Men Legends II: Rise of Apocalypse** for PC: `XMen2.exe` and the Alchemy
engine libraries it ships (`libIG*.dll`, `libMovie.dll`, `libCriMovie.dll`). It holds the pinned image
set, a symbol map from our own reverse engineering, and the RE notes. No source is matched yet.

The native port [xmen2](https://github.com/SomeoneIsWorking/xmen2) consumes this repository as a
submodule and reads its guest addresses from the symbol map.

## Bring your own install

No game bytes are ever committed here. Point the tools at your own installed copy:

```
uv run --frozen python tools/verify.py "<install dir>"
```

`config/images.toml` pins each image by size and SHA-256 and records its section table. The verifier
refuses an image that differs, and checks every symbol against the sections of its image: inside a
section, code names inside an executable one, no name or address twice.

## Layout

| path | what |
|---|---|
| `config/images.toml` | the images: file, size, SHA-256, image base, sections, symbol file |
| `config/symbols/<image>.txt` | the symbol map, splat `symbol_addrs` format (`name = 0xADDR; // type:func`) |
| `docs/notes/` | behaviour notes on guest routines and data |
| `docs/re-frontier.md` | the ordered RE evidence chain (`re_frontier.py` from re-harness) |
| `docs/prior-art.md` | other work on this build, licences and what we take |
| `docs/our-names.md` | addresses the port names more than once |
| `tools/verify.py` | the check above |

Notes cite xmen2 paths (`src/...`, `docs/issues/...`) where a port owner or an issue holds the evidence.

## Licence

MIT (`LICENSE`), covering this repository's own files only. X-Men Legends II is © Activision and
Marvel; nothing of it is distributed here.

Built with AI assistance (Claude and other LLMs).
