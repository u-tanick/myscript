import os
import glob
import shutil

# collect all image files in ./**/images
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

# marge all md files
with open('marge_md_list.conf', 'r') as f:
    md_file_lists = f.read().split("\n")

path = os.getcwd()
gen_file_name = "marged.md"

with open(gen_file_name, "w") as new_file:
    for count, md_file_name in enumerate(md_file_lists):
        if md_file_name:
            name = path + md_file_name
            print(name)
            with open(name, "r") as f:
                if count != 0:
                    new_file.write("\n\n")
                    new_file.write("<div class=\"page\" />")
                    new_file.write("\n\n")

                for line in f:
                    new_file.write(line)
        else:
            break

print("generate complete : " + gen_file_name)