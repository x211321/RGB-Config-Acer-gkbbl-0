#!/usr/bin/env python3

import os
import sys
import shutil
import tarfile
from zipfile import ZipFile

sys.path.append("../")

from lib.version import VERSION

BUILD_DIR  = "build"
BUNDLE_DIR = "RGB_Config_acer-gkbbl-0_v" + VERSION
TMPPGK_DIR = BUNDLE_DIR + "_tmp"
RPMPKG_DIR = BUNDLE_DIR + "_rpm"
DEBPKG_DIR = BUNDLE_DIR + "_deb"

# Find directory that contains this script
baseDir = os.path.abspath(os.path.dirname(__file__))

# cd to base dir
os.chdir(baseDir)

# Create build directory
if os.path.exists(BUILD_DIR):
    shutil.rmtree(BUILD_DIR)

os.makedirs(BUILD_DIR)

# cd to build dir
os.chdir(BUILD_DIR)

# Create bundle dir
os.makedirs(BUNDLE_DIR)




##########################
# Copy files to bundle dir
shutil.copy("../../rgb_config_acer_gkbbl_0.py", os.path.join(BUNDLE_DIR, "rgb_config_acer_gkbbl_0.py"))
shutil.copy("../../LICENSE"                   , os.path.join(BUNDLE_DIR, "LICENSE"))
shutil.copy("../../README.md"                 , os.path.join(BUNDLE_DIR, "README.md"))
shutil.copytree("../../lib/"                  , os.path.join(BUNDLE_DIR, "lib/"))
shutil.copytree("../../assets/"               , os.path.join(BUNDLE_DIR, "assets/"))

shutil.rmtree(os.path.join(BUNDLE_DIR, "lib/__pycache__/"))




###################
# Create tar bundle
with tarfile.open(BUNDLE_DIR + ".tar.gz", "w:gz") as tar:
    for root, dirs, files in os.walk(BUNDLE_DIR):
        for f in files:
            tar.add(os.path.join(root, f))

tar.close()




###################
# Create Zip bundle
zip = ZipFile(BUNDLE_DIR + ".zip", "w")

for root, dirs, files in os.walk(BUNDLE_DIR):
    for f in files:
        zip.write(os.path.join(root, f))

zip.close()




##################################################
# Create file structure for .deb and .rpm packages
os.makedirs(os.path.join(TMPPGK_DIR, "usr/local/bin"))
os.makedirs(os.path.join(TMPPGK_DIR, "usr/share/applications"))

# Copy previously bundled files to file structure / lib
shutil.copytree(BUNDLE_DIR + "/", os.path.join(TMPPGK_DIR, "usr/local/lib/rgb_config_acer_gkbbl_0/"))

# Copy start script to file structure / bin
shutil.copy("../rgb_config_acer_gkbbl_0", os.path.join(TMPPGK_DIR, "usr/local/bin/rgb_config_acer_gkbbl_0"))

# Copy .desktop application file to file structure / applications
shutil.copy("../rgb_config_acer_gkbbl_0.desktop", os.path.join(TMPPGK_DIR, "usr/share/applications/rgb_config_acer_gkbbl_0.desktop"))




#####################
# Create .deb package
os.makedirs(os.path.join(DEBPKG_DIR, "DEBIAN"))

# Copy previously bundled files to .deb structure
shutil.copytree(TMPPGK_DIR + "/usr", DEBPKG_DIR + "/usr")

# Write metadata
metaData =  "Package: rgb-config-acer-gkbbl-0\n" \
            "Version: " + VERSION + "\n" \
            "Section: base\n" \
            "Priority: optional\n" \
            "Architecture: all\n" \
            "Depends: python3-wxgtk4.0\n" \
            "Maintainer: x211321\n" \
            "Description: A simple GUI for controlling RGB settings of the Acer-WMI kernel module via the acer-gkbbl-0 character device\n" \
            "Homepage: https://github.com/x211321/RGB-Config-Acer-gkbbl-0\n"

file = open (os.path.join(DEBPKG_DIR, "DEBIAN/control"), "w", encoding="utf-8")
file.write(metaData)
file.close()

# Run dpkg-deb
os.system("dpkg-deb --build " + DEBPKG_DIR)

# Rename .deb package
os.rename(DEBPKG_DIR + ".deb", BUNDLE_DIR + ".deb")




#####################
# Create .rpm package

os.makedirs(os.path.join(RPMPKG_DIR, "SPECS"))

rpmProject = os.path.join(RPMPKG_DIR, "BUILDROOT/rgb_config_acer_gkbbl_0-"+VERSION+"-1.x86_64")

# Copy previously bundled files to .rpm structure
shutil.copytree(os.path.join(TMPPGK_DIR, "usr"), os.path.join(rpmProject, "usr"))

# Write .rpm spec
rpmspec = "Name:      rgb_config_acer_gkbbl_0\n" \
          "Version:   " + VERSION + "\n" \
          "Release:   1%{?dist}\n" \
          "Summary:   Control RGB settings of the Acer-WMI kernel module\n" \
          "BuildArch: noarch\n" \
          "\n" \
          "License:   MIT\n" \
          "URL:       https://github.com/x211321/RGB-Config-Acer-gkbbl-0\n" \
          "\n" \
          "Requires:  python3-wxpython4\n" \
          "\n" \
          "%description\n" \
          "A simple GUI for controlling RGB settings of the Acer-WMI kernel module via the acer-gkbbl-0 character device\n" \
          "\n" \
          "%files\n"

for root, dirs, files in os.walk(rpmProject):
    for f in files:
        rpmspec += os.path.join(root.replace(rpmProject, ""), f) + "\n"

file = open (os.path.join(RPMPKG_DIR, "SPECS/rgb-config-acer-gkbbl-0.spec"), "w", encoding="utf-8")
file.write(rpmspec)
file.close()

# Run rpmbuild
os.system("rpmbuild --define \"_topdir " + os.path.join(baseDir, BUILD_DIR, RPMPKG_DIR) + "\" -bb " + os.path.join(RPMPKG_DIR, "SPECS/rgb-config-acer-gkbbl-0.spec"))

# Move .rpm package to build folder
for root, dirs, files in os.walk(os.path.join(RPMPKG_DIR, "RPMS/noarch/")):
    for f in files:
        shutil.move(os.path.join(root, f), BUNDLE_DIR + ".rpm"), 
