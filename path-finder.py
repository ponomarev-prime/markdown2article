import os

prj_path = os.getcwd()
file_path = __file__

path_file = f"{prj_path}/path.ff"

open(path_file, 'w').close()
for l in (prj_path, file_path):
    with open(path_file, "a",encoding="utf-8") as file:
        file.write(f"{l}\n")