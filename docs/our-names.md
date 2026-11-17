# Our names

No upstream decomp exists, so every name in `config/symbols/` is ours. Where the port names one
address in more than one place, the map keeps the first and the others are listed here; the port
adopts the map's name when its constants are generated from the map.

| image | address | in the map | also used by the port | port file |
|---|---|---|---|---|
| XMen2.exe | `0x005D8920` | `MenuMgr_Get` | `MenuScene_MenuManager` | `src/native/menu_scene.cpp` |
| XMen2.exe | `0x005D8920` | `MenuMgr_Get` | `MenuStartOverride_MenuManager` | `src/native/menu_start_override.cpp` |
| XMen2.exe | `0x00680030` | `MenuFadeThreshold` | `TextItemTouch_StyleFadeThreshold` | `src/native/text_item_touch.cpp` |
| XMen2.exe | `0x00717AAC` | `ConversationPanel_Singleton` | `ScriptTrace_CONV_SINGLETON_VA` | `src/native/script_trace.cpp` |
