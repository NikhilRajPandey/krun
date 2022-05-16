#!/bin/python3
import sys
import os
from shutil import rmtree # Used to remove directory

# Extension Command
ext_command = {
    ".py" : "python3 %f",
    ".c" : "gcc %f -o .krun/%fw && ./.krun/%fw",
    ".cpp" : "g++ %f -o .krun/%fw && && ./.krun/%fw",
    ".sh" : "bash %f",
    ".html" : "firefox %f"
}

if not os.path.isdir('.krun'):
    os.mkdir(".krun")

file_path = sys.argv[1]
file_name = file_path.split('/')[-1]
file_name_without_ext = file_name.split('.')[0]
file_name_ext = '.' + file_name.split('.')[-1]

if file_name_ext not in ext_command.keys():
    sys.exit("File Not Supported")

executing_command = ext_command[file_name_ext]
executing_command = executing_command.replace("%fw",file_name_without_ext)
executing_command = executing_command.replace("%f",file_path)

print(executing_command)
os.system(executing_command)
rmtree('.krun')
