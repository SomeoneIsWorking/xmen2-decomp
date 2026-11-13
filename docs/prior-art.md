# Prior art for X-Men Legends II (PC)

Other work on this exact build: decompilations, symbol maps, mods and RE notes, each with its licence,
whether its addresses match our images (`config/images.toml`), and what we may take from it.

## Title prior art

External work on X-Men Legends II PC `XMen2.exe` (3,129,344 bytes, SHA-256 `146cd9c316edb57a267cd73753a7ce9af647e52aab750d449c6b278fb4a1669b`, PE timestamp `0x43203baf`, image base `0x00400000`; `libIG*.dll` at `0x10000000`), checked against our install with `objdump`.

| project | URL | kind | license | target build | build match (addresses checked) | what we may take | notes |
|---|---|---|---|---|---|---|---|
| XML2-MUA-Display-Mods (`research/OFFSETS-XML2.md`) | https://github.com/KaikoClanworth1/XML2-MUA-Display-Mods | RE notes for resolution, screen mode and window style | MIT | same 3,129,344-byte `XMen2.exe` | matched: `0x005fac45` calls `0x0061bf80` (resolution reader, function start); `0x005facb1` is `mov byte [edi+4],1` (forced fullscreen); `libIGDisplay.dll` `0x1000581a` `mov edi,0x06cf0000` and file offset `0x5809` holds `00 00 00 85` | evidence only (display and window facts) | Created 2026-06. |
| XML2-Modern-Controller | https://github.com/andreMeloo/XML2-Modern-Controller | controller proxy and analog hook DLL with build profile | MIT | SHA-256 identical to ours | matched: profile SHA-256, size, timestamp `0x43203BAF` and image size `0x006744C6` equal our exe; hook addresses not checked | evidence only (input path) | Created 2026-09. |
| xml2-debug-menu | https://github.com/KaikoClanworth1/xml2-debug-menu | ASI ImGui overlay; BehavEd command dispatch tables | none ("private" badge) | PC `XMen2.exe` | matched: `0x004d5830` (BehavEd `GetParam`, `__thiscall`) is a function start after `int3` padding; game-manager global `0x006f38f8` not checked | names only | Created 2026-03. Relevant to the command tables in `docs/RE/boot.md`. |
| xml2-fix | https://github.com/ChronoRixun/xml2-fix | drop-in `dinput.dll`: controllers, online play, crash guards | MIT | PC `XMen2.exe` (retail and Steam named) | matched: `XMen2.exe+0x1a6848` (team-combo popup) lies in `FUN_005a6500`, which formats two hero names and an XP award in our exe | copy with attribution (fixes and their addresses) | Created 2026-09, active. |
| XML2-32-Roster-Hack | https://github.com/viktorsosiktor/XML2-32-Roster-Hack | roster limit raise | Unlicense | PC `XMen2.exe` | not checked: no address or hash in the README | copy (public domain) | Created 2026-10. |
| x-men-legends-2-analogic | https://github.com/maebashimarcelo-prog/x-men-legends-2-analogic | analog stick hook | none stated (`NOASSERTION`) | SHA-256 identical to ours (README) | matched: SHA-256; hook addresses not checked | evidence only | Created 2026-10. |
| MUA.XML2.LimitAdjuster | https://github.com/nikita488/MUA.XML2.LimitAdjuster | limit adjuster (ThirteenAG framework) | MIT | Marvel Ultimate Alliance; XML2 has no profile in `limits/` | not applicable (MUA addresses only) | nothing | Last push 2020. |
| igBlender | https://github.com/ak2yny/igBlender | Blender plugin for Alchemy 5 IGB | GPL-3.0 | asset format | not applicable | evidence only (IGB format) | |
| igb-blender | https://github.com/KaikoClanworth1/igb-blender | Blender IGB/IGZ importer/exporter | none | asset format | not applicable | evidence only | |
| alchemy | https://github.com/SomeoneIsWorking/alchemy | our shared Alchemy layer | ours | asset format | not applicable | ours | |
| xmenlegends (Cwf1997), OpenXML1xbox, legends-classic | https://github.com/Cwf1997/xmenlegends | Xbox X-Men Legends (2004) decomp / recompilation | MIT / none / MIT | X-Men Legends 1 Xbox | not applicable (different game) | nothing | Shares the engine family only. |

Not found (searched 2026-10-13, again 2026-11-13 on GitHub and the web): a decompilation (matching or not) of X-Men Legends II on decomp.dev or GitHub for any platform; a public Ghidra or IDA database or symbol map for `XMen2.exe` or the `libIG*.dll` set; a PC recompilation. Codeberg search returned its anti-scraper page and was not checked.
