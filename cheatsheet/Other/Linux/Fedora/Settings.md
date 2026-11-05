# Settings

<style>hide {display: none;}</style>

<hide>
???
Display & Monitor -> Screen Edges
Maximize: [X]
Tile: [X]
Behavior: [ ]
Trigger quarter tiling in: Outer 25%
Switch desktop on edge: Disabled
Activation delay: 75ms
Reactivation delay: 350ms
Corner barrier: [X]
Edge barrier: 100px
</hide>

<hide>
[General Behavior]
[Plasma]
Allow Plasma to show: [X] Panel and widget tooltips
                      [X] OSD popups for status changes
[Scrolling]
Clicking in scrollbar track: (X) Scrolls to the clicked location
                             ( ) Scrolls one page up or down
                                 Middle-click to scroll to clicked location
                             [X] Prefer smooth scrolling
[Clicking]
Clicking files or folders: (X) Selects them
                               Open by double-clicking instead
                           ( ) Opens them
                               Select by clicking on item's selection marker
Middle-click: [X] Pastes selected text
Double-click interval: 400ms
-
Dragging files or folders: (X) Always ask what to do
Enable Tablet Mode: (X) Automatically enable as needed
</hide>

```json
{
    "Keyboard": {
        "Keyboard": {
            "NumLock on startup": "Turn on"
        },
        "Shortcuts": {
            "Add New -> Command": [
                {
                    "Name":     "%Y-%m-%d_%H-%M-%S.png",
                    "Command":  "bash -c 'source ~/.PYPRECODE/bin/activate && python -c \"__import__(\\\"pyperclip\\\").copy(f\\\"{__import__(\\\"datetime\\\").datetime.now():%Y-%m-%d_%H-%M-%S}.png\\\")\"'",
                    "Shortcut": "Meta+Shift+Y"
                },
                {
                    "Name":     "CUID",
                    "Command":  "bash -c 'source ~/.PYPRECODE/bin/activate && python -c \"__import__(\\\"pyperclip\\\").copy(str(__import__(\\\"uuid\\\").uuid4()).replace(\\\"-\\\", \\\"\\\")[:16])\"'",
                    "Shortcut": "Meta+Shift+U"
                },
                {
                    "Name":     "TOTP",
                    "Command":  "bash -c 'source ~/.PYPRECODE/bin/activate && python -c \"__import__(\\\"pyperclip\\\").copy(\\\"/totp code \\\"+__import__(\\\"pyotp\\\").TOTP(\\\"<TOKEN>\\\").now())\"'",
                    "Shortcut": "Meta+Shift+P"
                }
            ],
            "Window Management": {
                "Peek at Desktop": "No active shortcuts"
            },
            "Plasma Workspace": {
                "Activate Minimize All Windows Windget": "Meta+D",
                "Walk through activities": "Meta+A",
                "Walk through activities (Reverse)": "Meta+Shift+A"
            }
        }
    },
    "Accesibility": {
        "Zoom & Magnifier": [
            "( ) Full screen",
            "(X) Magnify region",
            "( ) Disabled"
        ],
        "Shake Pointer": {
            "Shake pointer to find it": "[ ] Enable"
        }
    },
    "Colors & Themes": {
        "Windows Decorations": "Windows 10 Light",
        "Pointers": "Windows10Light"
    },
    "Text & Fonts": {
        "Fonts": {
            "Sub-pixel rendering": "None"
        }
    },
    "Notifications": [
        "[ ] While a fullscreen application is focused"
    ],
    "Windows Management": {
        "Task Swither": {
            "Shortcuts": {
                "All windows": {
                    "Forward": "Alt+Tab or Meta+Tab",
                    "Reverse": "Meta+Shift+Tab or Alt+Shift+Tab"
                },
                "Current application": {
                    "Forward": "Alt+` or Meta+`",
                    "Reverse": "Meta+~ or Alt+~"
                }
            }
        },
        "Virtual Desktops": {
            "Rows": 1
        }
    },
    "Screen Locking": {
        "Lock screen automatically": [
            "10 minuted",
            "[X] Lock after waking from sleep"
        ]
    },
    "Power Management": {
        "On AC Power": {
            "When inactive": "Sleep | After 10 minutes"
        },
        "On Battery": {
            "Switch to power profile": "Power Save"
        },
        "On Low Battery": {
            "When inactive": "Sleep | After 1 minute",
            "Change screen brightness": "[X] 20%",
            "Switch to power profile": "Power Save"
        }
    }
}
```

```
# Windows rules
## Windows matching
Description:                 Windows settings for Picture in picture
Windows class (application): Unimportant | <empty>
Windows types:               Normal windows
Windows title:               Exact match | Picture in picture
## Size & Position
Position:                    Apply initially | 1535 x 935
Size:                        Apply initially | 367 x 200
initially placement:         Force | Default
## Arrangement & Access
Keep above other windows:    Force | (X) Yes
```

```
## Windows matching
Description:                 Application settings for Minecraft* 1.21.11
Windows class (application): Exact match | Minecraft* 1.21.11
Match whole windows class:   (X) No
Windows types:               All selected
## Size & Position
Position:                    Remember | 116 x 0
```

```
## Windows matching
Description:                 Window settings for Minecraft* 1.21.11
Windows class (application): Exact match | Minecraft* 1.21.11
Match whole windows class:   (X) No
Windows types:               Exact match | Minecraft* 1.21.11
## Size & Position
Position:                    Remember | 0 x 0
```

```
## Windows matching
Description:                 Windows settings for org.kde.discover
Windows class (application): Exact match | plasma-discover org.kde.discover
Match whole windows class:   (X) Yes
Windows types:               Normal windows
## Size & Position
Maximized horizontally:      Apply initially | (X) No
Maximized vertivally:        Apply initially | (X) No
```

```
KDE Menu Editor
[Development]
Name:                  IPython
Program:               konsole
Command-line argument: --hold -e bash -c 'source ~/.PYPRECODE/bin/activate && ipython -i ~/PYPRECODE.py'

Name:                  Python
Program:               konsole
Command-line argument: --hold -e bash -c 'source ~/.PYPRECODE/bin/activate && python -i ~/PYPRECODE.py'
```

```
[Internet]
Microsoft Edge (Web Browser)
Name:                  Microsoft Edge
Program:               /usr/bin/microsoft-edge-stable
Command-line argument: %U --enable-features=msForceNoRoundedCornerAndMargin --disable-features=msFeatureGroupNewLookAndFeelHoldout
```

```
Flatpak
Telegram
Discord
```
