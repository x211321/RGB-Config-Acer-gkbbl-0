import os
import lib.var as var
import json

# Load preferences
if not os.path.exists(var.PREFERENCE_DIR):
    os.makedirs(var.PREFERENCE_DIR)

# Set default preferences
app_preferences = {
    "tray"          : False,
    "log"           : True,
    "profiles"      : True,
    "preview"       : True,
    "startMinimized": False,
    "closeToTray"   : False,
    "applyStart"    : False,
    "extendSpeed"   : False,
    "language"      : ""
}

# Get path to preference file
pref_file = os.path.join(var.PREFERENCE_DIR, var.PREFERENCE_FILE)

if os.path.isfile(pref_file):
    # Read preferences from file and merge with default preferences
    with open(f"{pref_file}", 'rt') as file:
        app_preferences = {**app_preferences, **json.load(file)}
