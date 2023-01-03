import os
from pathlib import Path

def add_element(data: str, position: int):
    position = 0
    data = 'Konev'
    name_file = '/db/db'
    file_path = Path(os.getcwd() + name_file, os.getcwd() + name_file + '.txt')
    with open(file_path, 'a', encoding="utf-8") as data_write:
        data_write.write(f'\n{data}')

add_element('Konev',0)