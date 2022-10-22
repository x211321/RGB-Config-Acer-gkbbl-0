#  RGB-Config-Acer-gkbbl-0
A simple GUI for controlling RGB settings of the **Acer-WMI kernel module** via the **acer-gkbbl-0** character device

Visit JafarAkhondali's [project page](https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module) for information on the kernel module

![Main window](./img/screenshots/main_window.png)

# Features
 * Configure RGB settings of the Acer-WMI kernel module via the acer-gkbbl-0 character device
 * Supports all available RGB modes (Static, Breath, Neon, Wave, Shifting and Zoom)
 * Settings can be saved as profiles
 * Tray icon for quick profile change (on supported systems)
 * Last used settings can be automatically restored upon application start
 * Animated preview for selected RGB mode 

# Restrictions
 * Compatible Acer-WMI kernel module **must be installed separately**
 * Compatibility depends on the specific laptop model and its compatibility with the kernel module
 * The tray icon only works in desktop environments that are compatible with classic system tray

# Installation
> ⚠ Make sure you have the **acer-gkbbl-0** RGB device available before you proceed with the installation of this application, otherwise it will have no effect. Visit JafarAkhondali's [project page](https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module) for more information on the needed kernel module.

> **RGB-Config-Acer-gkbbl-0** is written in Python3, using the wxPython framework. Python3 is usually provided by most Linux distributions, wxPython must often be installed separately.

---

## Debian / Ubuntu / Linux Mint / Pop!_OS
For systems that use the **apt package manager** a **.deb** package is provided. Simply download the **.deb** file from the [releases page](https://github.com/x211321/RGB-Config-Acer-gkbbl-0/releases) and run the installation. In many systems **.deb** files can run directly from the file manager by (double) clicking.

**Alternatively install the application from the command line:**
```
sudo dpkg -i ./RGB_Config_acer-gkbbl-0_v<VERSION>.deb
```

---

## Fedora
A Fedora specific **.rpm** package can be found on the [releases page](https://github.com/x211321/RGB-Config-Acer-gkbbl-0/releases). Download the file that ends on **_fedora.rpm**. Most setups should allow the execution of **.rpm** files via the file manager.

**Alternatively install the application from the command line:**
```
sudo dnf install ./RGB_Config_acer-gkbbl-0_v<VERSION>.rpm
```

---

## openSUSE Leap
> ⚠ Under openSUSE the package must be installed from command line because the package is not signed.

A openSUSE **Leap** specific **.rpm** package can be found on the [releases page](https://github.com/x211321/RGB-Config-Acer-gkbbl-0/releases). Download the file that ends on **_openSUSE_Leap.rpm**.

**Install the application by running the following command from the command line:**
```
sudo zypper install ./RGB_Config_acer-gkbbl-0_v<VERSION>_openSUSE_Leap.rpm
```

**zypper** will show a warning:

```
Package header is not signed!
Signature verification failed [6-File is unsigned]
```

Input **I** (ignore) to continue with the installation.

---

## openSUSE Tumbleweed
> ⚠ Under openSUSE the package must be installed from command line because the package is not signed.

A openSUSE **Tumbleweed** specific **.rpm** package can be found on the [releases page](https://github.com/x211321/RGB-Config-Acer-gkbbl-0/releases). Download the file that ends on **_openSUSE_TW.rpm**.

**Install the application by running the following command from the command line:**
```
sudo zypper install ./RGB_Config_acer-gkbbl-0_v<VERSION>_openSUSE_TW.rpm
```

**zypper** will show a warning:

```
Package header is not signed!
Signature verification failed [6-File is unsigned]
```

Input **I** (ignore) to continue with the installation.

---

## Arch Linux / Manjaro
For Arch Linux based systems that use the pacman package manager a PKGBUILD is provided. Download the file that ends on **_PKGBUILD.tar.gz** from the [releases page](https://github.com/x211321/RGB-Config-Acer-gkbbl-0/releases). 

The installation will proceed via the command line:

**Extract the archive**
```
tar -xf RGB_Config_acer-gkbbl-0_v<VERSION>_PKGBUILD.tar.gz
```

**Change into the newly extracted folder**
```
cd RGB_Config_acer-gkbbl-0_v<VERSION>_PKGBUILD
```

**Run makepkg with external dependencies and install the package via pacman**
```
makepkg -si
```

# Usage
After installation **RGB Config (acer-gkbbl-0)** should show up in your application launcher under both the **Settings** and **Utils** sections. 

Alternatively run the application from the command line:

```
rgb_config_acer_gkbbl_0
```

# Python script
Follow these steps in case none of the above installation methods work for you or you want to run the Python script directly without installation.

Download the **RGB_Config_acer-gkbbl-0_\<VERSION>.tar.gz** file from the [releases page](https://github.com/x211321/RGB-Config-Acer-gkbbl-0/releases) and extract it somewhere on your hard drive.

The required dependencies can be installed via your distributions package manager.

**Debian / Ubuntu / Linux Mint / Pop!_OS**
```
sudo apt install python3-wxgtk4.0
```

**Fedora**
```
sudo dnf install python3-wxpython4
```

**openSUSE Leap**
```
sudo zypper install python3-wxPython
```

**openSUSE Tumbleweed**
```
sudo zypper install python310-wxPython
```

**Arch Linux**
```
sudo pacman -S python-wxpython
```

**After that you should be able to start the application by running:**
```
./rgb_config_acer_gkbbl_0.py
```

**Or alternatively:**
```
python3 ./rgb_config_acer_gkbbl_0.py
```

# Options
![Options](./img/screenshots/options.png)

## Show tray icon
Display a tray icon in the notification area where to **RGB-Config-Acer-gkbbl-0** can be hidden. The tray icon also provides quick access to saved profiles. 
 * Left click on the tray icon to hide or restore **RGB-Config-Acer-gkbbl-0**
 * Right click to show the tray menu
 * The tray icon only works in desktop environments that are compatible with classic system tray (it does **not** work on a stock Gnome 3 installation).
 * The tray icon has been tested to work on the following desktop environments:
   * KDE (X11), LXQT, LXDE, XFCE, MATE, Cinnamon, Gnome Flashback, Gnome3 Pop!_OS

![Tray menu](./img/screenshots/tray_menu.png)

## Start minimized
Automatically hide application upton start. Intended for setups where the application is run on boot up (e.g. placed in your desktops auto start).

 * Only activate this option when your system is compatible with the tray icon. Otherwise the application will be permanently hidden. 
 * Should the need arise, options can be turned off in the config file: 
   * **~/.config/rgb_config_acer_gkbbl_0/preferences.json**

## Close to tray
Hide the application to tray instead of closing it when the close button in the title bar is pressed. 

## Apply [ACTIVE] on startup
Automatically apply the last used RGB settings when the application is started. See the "Profiles" section for more information regarding profiles.

## Extend max speed
Official Acer software only allows animation speeds between 0 and 9. The **acer-gkbbl-0** character device actually accepts values between 0 and 255, which depending on your specific system may or may not have an effect. Since speed values above 9 are not officially supported they are hidden by default. The "Extend max speed" option extends the speed range from 0-9 to 0-255. Results may vary.

# Profiles

## Save profiles
RGB settings can be saved as profiles. Simply configure your preferred settings and click on the **Save as profile** button. The application will ask for a profile name and store it in the profile directory.

## Load profiles
Saved profiles are listed in the profile list on the right side of the application. Click on a profile and press the **Load** button to restore the profile settings. Loaded profiles are **not** automatically applied to the character device and must first be activated via the **Apply** button. 

 * Profiles that are selected via the tray icon are directly applied and must not be activated separately.

## Delete profiles
Select the profile you want to delete from the profile list and press the **Delete** button. The profile will be removed from the profile directory.

## The [ACTIVE] profile
The [ACTIVE] profile is automatically generated whenever settings are written to the character device. The [ACTIVE] profile thus represents the last used settings and is automatically restored whenever the application is started.

## Compatibility with facer_rgb.py
The profiles that this application generates are compatible with the **facer_rgb** script that is provided by JafarAkhondali's **acer-predator-turbo-and-rgb-keyboard-linux-module**, with the exception of static mode for which **RGB-Config-Acer-gkbbl-0** has implemented multiple colors per profile (one for each section of the keyboard). A static mode profile that was generated with **RGB-Config-Acer-gkbbl-0** would only apply the color of the first section when run with **facer_rgb**.

## Profile directory
In compatibility with facer_rgb, profiles are stored in:
```
~/.config/predator/saved profiles/
```

# Configuration file
RGB-Config-Acer-gkbbl-0 saves user preferences in:
```
~/.config/rgb_config_acer_gkbbl_0/preferences.json
```

# Dev instructions

## General structure
 * The UI was designed with **wxFormBuilder**
 * Open **ui.fbp** in **wxFormBuilder** to make changes to the UI
 * All application logic is handled in **rgb_config_acer_gkbbl_0.py**, mainly in the **AcerRGBGUI_Frame** class
 * The **lib/ui.py** file is automatically generated by **wxFormBuilder** and should **not** be edited manually
 
## The "scripts" folder
The "scripts" folder contains the **build_linux.py** script which generates the **.zip**, **.tar.gz**, **.deb** and **.rpm** files that are attached to the release page. 

Also included are the **rgb_config_acer_gkbbl_0** shell script (which is placed in **/usr/bin/** when installed via the **.deb/.rpm** package) and the **rgb_config_acer_gkbbl_0.desktop** file (which gets installed under **/usr/share/applications/**).

The .deb/.rpm packages installs the actual application files to **/usr/lib/rgb_config_acer_gkbbl_0/**.

## i18n
**RGB-Config-Acer-gkbbl-0** has support for multiple languages. Available languages can be found in the **assets/locale/** folder. 

To update the translation files run the **i18n_gen.py** script in the **scripts** folder.

To add a new language, extend the **languages** list at the top of the **i18n_gen.py** script with the two letter language code you want to add and run the script. A new translation template will be generated at:

```
assets/locale/<LANGUAGE>/LC_MESSAGES/rgb_config_acer_gkbbl_0.po
```

This translation template can be loaded with a compatible software like Poedit.

Once saved in Poedit, the new language will show up in the Options menu of **RGB-Config-Acer-gkbbl-0**. Poedit automatically generates the compiled **.mo** language file that is used by the program code.

## Dev dependencies

**Libraries**
 * wxPython
 * Python3
 * Python3-polib
 
**Tools**
 * wxFormBuilder
 * Poedit
 * rpmbuild
 * dpkg-deb
 
**Debian/Ubuntu/Mint**
```
sudo apt install python3-wxgtk4.0 python3-polib rpm 
```





