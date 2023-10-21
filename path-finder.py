import os
import configparser


prj_path = os.getcwd()
file_path = __file__
path_file = f"{prj_path}/path.ff"
md_origin_path = f"{prj_path}/data/markdown_origin"
html_processed_path = f"{prj_path}/data/html"

config = configparser.ConfigParser()

config.add_section('PATH')
config.set('PATH', 'cwd_path', prj_path)
config.set('PATH', 'scr_path', file_path)
config.set('PATH', 'art_path', md_origin_path)
config.set('PATH', 'htm_path', html_processed_path)

with open(path_file, "w", encoding="utf-8") as file:
    config.write(file)