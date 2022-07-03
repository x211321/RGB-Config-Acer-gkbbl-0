#!/usr/bin/env python3

import os
import shutil
import polib

languages = ["en_US", "de_DE"]

files = []

path = "../"

file_list = os.listdir(path)

for file in file_list:
    if file.endswith(".py"):
        files.append(path+file)

print("Generating .po for:")
for file in files:
    print(file)

path = "../locale/"

if not os.path.exists(path):
    os.makedirs(path)

os.system("pygettext3 -d base -o ./base.pot " + " ".join(files))

for language in languages:

    targetPath = path + language + "/LC_MESSAGES/"

    if not os.path.exists(targetPath):
        os.makedirs(targetPath)

    if os.path.exists(targetPath+"base.po"):
        # Newly generated template
        pot_file = polib.pofile("./base.pot")

        # Existing translation
        po_file = polib.pofile(targetPath + "base.po")

        # Merge
        po_file.merge(pot_file)

        # Save
        po_file.save(targetPath + "base.po")
    else:
        # New translation
        # Copy
        shutil.copyfile("./base.pot", targetPath+"base.po")

