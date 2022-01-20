#-------------------------------------------------------------------------------
# Name:        Compare HTML files
# Purpose:    
#
# Author:      nicolescu
#
# Created:     20/01/2022
# Copyright:   (c) nicol 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import difflib
import os
import sys
from pathlib import Path
import shutil
import time



ts = time.time()

fold1_path = input(r"Address of first folder:")
list1 = list(Path(fold1_path).glob("*.html"))

## Create empty folder
x = os.path.expanduser("~")+ r"\Desktop\script_result"
path = x
if not os.path.exists(path):
    os.makedirs(path)

# Copy files to new folder for compare
files = list1.copy()
for f in files:
    shutil.copy(f, path)

fold2_path = input(r"Address of second folder:")
list2 = list(Path(fold2_path).glob("*.html"))

def compare(folder1, folder2):
    for num in range(len(list1)):
        show_pre = "Before editing:"
        show_post = "After editing:"
        show_pre_lines = open(folder1[num]).readlines()
        show_post_lines = open(folder2[num]).readlines()
        difference = difflib.HtmlDiff(wrapcolumn = 90).make_file(show_pre_lines, show_post_lines, show_pre, show_post)

    for file in range(len(folder1)):
        difference_report = open(folder1[file], "w+")
        difference_report.write(difference)
        difference_report.close()

fold3_path = list(Path(x).glob("*.html"))

compare(fold3_path, list2)

te = time.time()
total_time = te-ts
print("Script done!")
print("Total time used: {:10.2f}".format(total_time))

exit_on_enter = input("Press ENTER to exit...")
print(exit_on_enter)

