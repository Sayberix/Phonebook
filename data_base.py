from pathlib import Path
from os import getcwd

name_file = '/db/db'

def add_element(data: str, name_file: str):
    data = 'Konev'
    file_path = Path(getcwd() + name_file, getcwd() + name_file + '.txt')
    with open(file_path, 'a', encoding="utf-8") as data_write:
        data_write.write(f'\n{data}')

def read_element(name_file: str):
    file_path = Path(getcwd() + name_file, getcwd() + name_file + '.txt')
    with open(file_path, 'r', encoding="utf-8") as data_read:
        return data_read.readlines()

#add_element('Konev', name_file)
print(read_element(name_file))