import pathlib

# Preferences
PREFERENCE_DIR  = str(pathlib.Path.home()) + "/.config/rgb_config_acer_gkbbl_0"
PREFERENCE_FILE = "preferences.json"

# Kernel module
MODULE_DOWNLOAD_PATH = PREFERENCE_DIR + "/kernel_module_src.zip"
MODULE_EXTRACT_PATH  = PREFERENCE_DIR + "/kernel_module_src"

MODULE_WEBSITE  = "https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module"
MODULE_DOWNLOAD = "https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module/archive/refs/heads/main.zip"

MODULE_INSTALL_SYSTEMD   = "install_service.sh"
MODULE_INSTALL_OPENRC    = "install_openrc.sh"
MODULE_INSTALL_NOSERVICE = "install.sh"

MODULE_UNINSTALL_SYSTEMD   = "install_service.sh remove"
MODULE_UNINSTALL_OPENRC    = "install_openrc.sh remove"
MODULE_UNINSTALL_NOSERVICE = "uninstall.sh"

MODULE_INITSYSTEM_SYSTEMD  = "Systemd"
MODULE_INITSYSTEM_OPENRC   = "OpenRC"
MODULE_INITSYSTEM_SYSVINIT = "SysVinit"

SUPPORTED_DEVICES = [
    "AN515-45",
    "AN515-55",
    "AN515-57",
    "AN515-58",
    "AN517-41",
    "PH315-52",
    "PH315-53",
    "PH315-54",
    "PH315-55",
    "PH317-53",
    "PH317-54",
    "PH517-51",
    "PH517-52",
    "PH517-61",
    "PH717-71",
    "PH717-72",
    "PT314-51",
    "PT315-51",
    "PT314-52S",
    "PT315-52",
    "PT515-51",
    "PT515-52",
    "PT516-52s",
    "PT917-71"
]

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

GREEN  = (000, 200, 000, 255)
BLUE   = (000, 000, 200, 255)
YELLOW = (200, 200, 000, 255)
RED    = (200, 000, 000, 255)