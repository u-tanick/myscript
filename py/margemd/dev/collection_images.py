import os
import glob
import shutil
import subprocess

dest_dir = 'images'
if os.path.exists(dest_dir):
    shutil.rmtree(dest_dir)
os.mkdir(dest_dir)

for folder in glob.glob('**/images', recursive=True):
    print(folder)
    list_file_name = os.listdir(folder)
    print(list_file_name)
    for i_file_name in list_file_name:
        join_name = os.path.join(folder, i_file_name)
        if os.path.isfile(join_name):
            shutil.copy(join_name, dest_dir)
        else:
            shutil.copytree(join_name, os.path.join(dest_dir, i_file_name))



# shutil.rmtree(dest_dir)
