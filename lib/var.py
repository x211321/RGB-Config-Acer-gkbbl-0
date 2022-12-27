import pathlib

# Preferences
PREFERENCE_DIR  = str(pathlib.Path.home()) + "/.config/rgb_config_acer_gkbbl_0"
PREFERENCE_FILE = "preferences.json"

# Tray icon styles
TRAY_ICON_STYLE_DIR         = "./assets/tray"
TRAY_ICON_STYLE_MENU_OFFSET = 300

# RGB-Mode constants
RGB_MODE_STATIC   = 0
RGB_MODE_BREATH   = 1
RGB_MODE_NEON     = 2
RGB_MODE_WAVE     = 3
RGB_MODE_SHIFTING = 4
RGB_MODE_ZOOM     = 5

# Payload sizes
RGB_PAYLOAD_SIZE         = 16
RGB_STATIC_PAYLOAD_SIZE  = 4

# RGB kernel devices
RGB_DEVICE        = "/dev/acer-gkbbl-0"
RGB_DEVICE_STATIC = "/dev/acer-gkbbl-static-0"

# Profile directory
#   profiles are ment to be compatible with the facer_rgb.py script
#   that comes with JafarAkhondali's kernel module
#   https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module
PROFILE_DIR = str(pathlib.Path.home()) + "/.config/predator/saved profiles"

# Miscellaneous constants
ACTIVE_PROFILE     = "[ACTIVE]"
PROFILE_EXTENSION  = ".json"