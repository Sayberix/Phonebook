from pathlib import Path
from parameters import name_file

def add_element(data: str, name_file: str):
    data = 'Konev'
    file_path = Path(name_file, name_file + '.txt')
    with open(file_path, 'a', encoding="utf-8") as data_write:
        data_write.write(f'\n{data}')

def read_element(name_file: str) -> str:
    file_path = Path(name_file, name_file + '.txt')
    with open(file_path, 'r', encoding="utf-8") as data_read:
        return data_read.read().splitlines()

#add_element('Konev', name_file)
#print(read_element(name_file))