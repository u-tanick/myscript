import os

with open('mdlist.conf', 'r') as f:
    md_file_lists = f.read().split("\n")

path = os.getcwd()
gen_file_name = "new.md"

with open(gen_file_name, "w") as new_file:
    for md_file_name in md_file_lists:
        if md_file_name:
            name = path + md_file_name
            print(name)
            with open(name, "r") as f:
                for line in f:
                    new_file.write(line)
         
            new_file.write("\n\n")
            new_file.write("<div class=\"page\" />")
            new_file.write("\n\n")
        else:
            break

print("generate complete : " + gen_file_name)