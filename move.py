import os
import shutil

#Get the directory, the move.py-file is in
path_1 = __file__
path_2 = os.path.dirname(path_1) + '/'
dateityp = input("Welchen Dateityp willst du sortieren?(ohne'.'): ")
folder_name = dateityp

# Get the list of all files and directories
dir_list = os.listdir(path_2)

#if folder with extention name does not exist, create
if not os.path.exists(path_2 + folder_name):
        os.makedirs(path_2 + folder_name)

#scan for files with extension and move to folder

for files in dir_list:
    
    if ("."+dateityp) in files and not os.path.exists(path_2 + folder_name + '/' + files):
        shutil.move(path_2 + files, path_2 + folder_name + '/' +files)
    
    else:
        continue
print("done")
