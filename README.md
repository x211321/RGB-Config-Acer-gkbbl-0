#  RGB-Config-Acer-gkbbl-0
A simple GUI for controlling the RGB settings of the acer-gkbbl-0 kernel module

![Main window](./screenshots/main_window.gif)

# Features
 * Configure RGB settings of the acer-gkbbl-0 kernel module
 * Supports all available RGB modes (Static, Breath, Neon, Wave, Shifting and Zoom)
 * Settings can be saved as profiles
 * Tray icon for quick profile change (on supported systems)
 * Auto apply of last used settings on startup
 * Animated preview for selected RGB mode 

# Restrictions
 * acer-gkbbl-0 kernel module must be installed separately
 * Compatibility depends on the specific laptop model and its compatibility with the acer-gkbbl-0 kernel module
 * The "static" RGB mode does not work with my specific laptop and is thus untestet
 * The tray icon only works in desktop environments that are compatible with classic system tray

# Installation
Make sure you have the acer-gkbbl-0 kernel module installed before you proceed with the installation of RGB-Config-Acer-gkbbl-0. Visit JafarAkhondalis project page for more information on the kernel module. https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module

RGB-Config-Acer-gkbbl-0 is written in Python3, using the wxPython framework. Python3 is usually provided by most Linux distributions, wxPython must often be installed separately.

## .deb package
For Debian based distributions (Ubuntu, Mint, etc.) a .deb package is provided. Your system's package manager will manage all necessary dependencies.

Download the **RGB_Config_acer-gkbbl-0_deb.deb** file from the [releases page](https://github.com/x211321/RGB-Config-Acer-gkbbl-0/releases). Depending on your system you can install the .deb file by double clicking it in your file manager or alternatively install it via the command line.

```
sudo dpkg -i RGB_Config_acer-gkbbl-0_deb.deb
```
After installation RGB-Config-Acer-gkbbl-0 should show up in your application launcher under the "Settings" and "Utils" sections. 

Alternatively run RGB-Config-Acer-gkbbl-0 from the command line:

```
rgb_config_acer_gkbbl_0
```

## Python script
Python 3 should already be provided by most Linux distributions.

Download the **RGB_Config_acer-gkbbl-0_script.zip** file from the [releases page](https://github.com/x211321/RGB-Config-Acer-gkbbl-0/releases) and extract it somewhere on your hard drive.

The required dependencies can be installed via your distributions package manager.

Debian/Ubuntu/Mint
```
sudo apt install python3-wxgtk4.0
```

Arch Linux
```
sudo pacman -S python-wxpython
```
After that you should be able to start the application by running:
```
./rgb_config_acer_gkbbl_0.py
```

Or alternatively:
```
python3 ./rgb_config_acer_gkbbl_0.py
```

# Options
![Options](./screenshots/options.png)

## Show tray icon
Display a tray icon in the system tray where to RGB-Config-Acer-gkbbl-0 can be hidden. The tray also provides quick access to saved profiles. Left click on the tray icon to hide or restore RGB-Config-Acer-gkbbl-0. Right click to show the tray menu. The tray icon only works in desktop environments that are compatible with classic system tray (e.g. it did not show on a fresh ubuntu install).

![Tray menu](./screenshots/tray_menu.png)

## Start minimized
Automatically hide application uppon start. Indended for setups where RGB-Config-Acer-gkbbl-0 is run on bootup (e.g. placed in your desktops auto start).

## Close to tray
Hide RGB-Config-Acer-gkbbl-0 to tray instead of closing it when the close button in the title bar is pressed. 

## Apply [ACTIVE] on startup
Auomatically apply the last used RGB settings when the application is started. See section "Profiles" for more information regarding profiles.

## Extend max speed
Official Acer software only allows animation speeds between 0 and 9. The acer-gkbbl-0 kernel module actually accepts values between 0 and 255, which depending on your specific system may or may not have an effect. Since speed values above 9 are not officially supported they are hidden by default. The "Extend max speed" option extends the speed range from 0-9 to 0-255. Results may vary.

# Profiles

## Save profiles
RGB settings can be saved as profiles. Simply configure your prefered settings and click on the "Save as profile" button. The application will ask for a profile name and store it in the profile directory.

## Load profiles
Saved profiles are listed in the profile list on the right side of the application. Click on a profile and press the "Load" button to restore the profile settings. Loaded profiles are **not** automatically applyed to the kernel device and must first be activated via the "Apply" button. 

Profiles that are selected via the tray icon are directly applied and must not be activated separately.

## Delete profiles
Select the profile you want to delete from the profile list and press the "Delete" button. The profile will be removed from the profile directory.

## The [ACTIVE] profile
The [ACTIVE] profile is automatically generated whenever RGB settings are applied. The [ACTIVE] profile thus represents the last used settings and is automatically restored whenever the RGB-Config-Acer-gkbbl-0 is started.

## Compatibility with facer_rgb.py
The profiles that RGB-Config-Acer-gkbbl-0 generates are compatible with the facer_rgb script that is provided by  JafarAkhondalis "acer-predator-turbo-and-rgb-keyboard-linux-module" project, with the exeption of static mode for which RGB-Config-Acer-gkbbl-0 has implemented muliple colors per profile. A static mode profile that was generated with RGB-Config-Acer-gkbbl-0 would only apply the first color when run with facer_rgb.

## Profile directory
Profiles are stored in:
```
~/.config/predator/saved profiles/
```

# Configuration file
RGB-Config-Acer-gkbbl-0 saves user preferences in:

```
~/.config/rgb_config_acer_gkbbl_0/preferences.json
```

