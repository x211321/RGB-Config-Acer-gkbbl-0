#!/usr/bin/env python3

import os
import shutil
import polib

LANG_DOMAIN = "rgb_config_acer_gkbbl_0"

languages = ["en", "de"]

files = []

path = "../"

file_list = os.listdir(path)

for file in file_list:
    if file.endswith(".py"):
        files.append(path+file)

path = "../lib/"

file_list = os.listdir(path)

for file in file_list:
    if file.endswith(".py"):
        files.append(path+file)

print("Generating .po for:")
for file in files:
    print(file)

path = "../assets/locale/"

if not os.path.exists(path):
    os.makedirs(path)

os.system("pygettext3 -d " + LANG_DOMAIN + " -o " + path + LANG_DOMAIN + ".pot " + " ".join(files))

for language in languages:

    targetPath = path + language + "/LC_MESSAGES/"

    if not os.path.exists(targetPath):
        os.makedirs(targetPath)

    if os.path.exists(targetPath+LANG_DOMAIN + ".po"):
        # Newly generated template
        pot_file = polib.pofile(path + LANG_DOMAIN + ".pot")

        # Existing translation
        po_file = polib.pofile(targetPath + LANG_DOMAIN + ".po")

        # Merge
        po_file.merge(pot_file)

        # Save
        po_file.save(targetPath + LANG_DOMAIN + ".po")
    else:
        # New translation
        # Copy
        shutil.copyfile(path + LANG_DOMAIN + ".pot", targetPath + LANG_DOMAIN + ".po")
