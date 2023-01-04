#!/usr/bin/python
 # -*- coding: utf-8 -*-

import data_base as db
from parameters import name_file

list_phone = []
list_phone = db.read_element(name_file)

# получение записи строки в виде списка
def get_element_list(list_phone_func: list, position_in_list: int) -> list:
    return list_phone_func[position_in_list].split(';')

# получение всех записей строк в виде списка
def get_all_element_list(list_phone_func: list) -> list:
    for i in range(len(list_phone_func)):
        print(get_element_list(list_phone_func,i))

# добавление записей в строку
def add_element_in_list(text: str) -> str:
    text += ';'
    return text

# поиск слова по всему списку справочника и вывод его позиции
def find_word_in_list(list_phone_func: list, text_word: str) -> tuple:
    for i in range(len(list_phone_func)):
        entry = get_element_list(list_phone_func,i)
        for j in range(len(entry)):
            if entry[j] == text_word:
                return (i, j)
    return(-1, -1)

#get_element_list(list_phone,0)
#get_all_element_list(list_phone)
print(find_word_in_list(list_phone,'Maxim'))