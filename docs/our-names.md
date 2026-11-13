# Our names

No upstream decomp exists, so every name in `config/symbols/` is ours. Where the port names one
address in more than one place, the map keeps the first and the others are listed here; the port
adopts the map's name when its constants are generated from the map.

| image | address | in the map | also used by the port | port file |
|---|---|---|---|---|
| XMen2.exe | `0x0046DCE0` | `ConversationPanel_GameOwner` | `ExtractionRevive_PartySingleton` | `src/native/extraction_revive.cpp` |
| XMen2.exe | `0x00597C20` | `MenuText_Fonts` | `PopupTouch_Fonts` | `src/native/popup_touch.cpp` |
| XMen2.exe | `0x0059EE20` | `ConversationTouch_WorldScene` | `PopupTouch_WorldScene` | `src/native/popup_touch.cpp` |
| XMen2.exe | `0x005BFCD0` | `ListTouch_EntryText` | `TeamTouch_EntryText` | `src/native/team_touch.cpp` |
| XMen2.exe | `0x005D8920` | `CutscenePlayer_FN_INPUT` | `MenuScene_MenuManager` | `src/native/menu_scene.cpp` |
| XMen2.exe | `0x005D8920` | `CutscenePlayer_FN_INPUT` | `MenuStartOverride_MenuManager` | `src/native/menu_start_override.cpp` |
| XMen2.exe | `0x005D8920` | `CutscenePlayer_FN_INPUT` | `OptionsMenuNoAdvanced_MenuManager` | `src/native/options_menu_no_advanced.cpp` |
| XMen2.exe | `0x005D8920` | `CutscenePlayer_FN_INPUT` | `PopupTouch_MenuManager` | `src/native/popup_touch.cpp` |
| XMen2.exe | `0x005EF270` | `ConversationTouch_TextLine` | `PopupTouch_TextLine` | `src/native/popup_touch.cpp` |
| XMen2.exe | `0x00680030` | `PopupTouch_PromptTimeout` | `TextItemTouch_StyleFadeThreshold` | `src/native/text_item_touch.cpp` |
| XMen2.exe | `0x00685CA4` | `ConversationTouch_LineFormat` | `PopupTouch_LineFormat` | `src/native/popup_touch.cpp` |
| XMen2.exe | `0x0069A444` | `MenuText_LineProbe` | `PopupTouch_LineProbe` | `src/native/popup_touch.cpp` |
| XMen2.exe | `0x006F3920` | `MenuAction_MenuPlayer` | `TeamTouch_MenuPlayer` | `src/native/team_touch.cpp` |
| XMen2.exe | `0x00717AAC` | `ConversationPanel_Singleton` | `ScriptTrace_CONV_SINGLETON_VA` | `src/native/script_trace.cpp` |
| XMen2.exe | `0x008A61C8` | `AutomapTouch_MapScale` | `HudMinimap_Scale` | `src/native/hud_minimap.cpp` |
