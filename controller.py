#!/usr/bin/python
 # -*- coding: utf-8 -*-

import data_base as db
from parameters import name_file

list_phone = []
list_phone = db.read_element(name_file)

# получение записи строки в виде списка (внутренняя ф-ция)
def get_element_list(position_in_list: int) -> list:
    global list_phone
    return list_phone[position_in_list].split(';')

# шапка колонок
def column_header():
    return ['Фамилия','Имя','Телефон','Описание']

# представление в удобочитаемой форме
def view_list():
    global list_phone
    [print(list_phone[i], ' | ', end=' ') if i < len(list_phone) - 1 else print(list_phone[i], ' | ', '\n') for i in range(len(list_phone)) ]
        
# просмотр всех записей
def view_all_list():
    global list_phone
    [view_list(get_element_list(list_phone,i)) for i in range(len(list_phone))]

# добавление записей в строку
def add_record_in_list() -> str:
    return str(input('Введите фамилию: ')) + ';' + str(input('Введите имя: ')) + ';' + str(input('Введите телефон: ')) + ';' + str(input('Введите описание: ')) + '\n'

# удаление записи по ключевому слову
def delete_record_in_list(text_word: str) -> str:
    global list_phone
    resault = ''
    for i in range(len(list_phone)):
        entry = get_element_list(list_phone,i)
        for j in entry:
            find_word = False
            if text_word in j:
                find_word = True
                print(view_list(entry))
                for_delete = 'Y'
                for_delete = str(input('Вам нужна эта запись для удаления? (Y/n):'))
                if for_delete == 'Y' or for_delete == "":
                    print("Запись удалена!")
                    break
        if find_word == False:
            resault += ";".join(entry) + '\n'
    db.write_element('w', resault, name_file)

# редактирование записи по ключевому слову
def editing_record_in_list(text_word: str) -> str:
    global list_phone
    resault = ''
    for i in range(len(list_phone)):
        entry = get_element_list(list_phone,i)
        for j in entry:
            find_word = False
            if text_word in j:
                find_word = True
                print(view_list(entry))
                for_delete = 'Y'
                for_delete = str(input('Вам нужна эта запись для редактирования? (Y/n):'))
                if for_delete == 'Y' or for_delete == "":
                    resault += add_record_in_list()
                    print("Запись отредактирована!")
                    break
        if find_word == False:
            resault += ";".join(entry) + '\n'
    db.write_element('w', resault, name_file)

# поиск слова по всему списку справочника и запись его позиции в список кортежей
def find_word_in_list(text_word: str) -> list[tuple]:
    global list_phone
    resault = []
    for i in range(len(list_phone)):
        entry = get_element_list(list_phone,i)
        for j in range(len(entry)):
            if entry[j] == text_word:
                tuple_rec = (i, j)  # где i - это номер строки а j - номер записи в строке
                resault.append(tuple_rec)
    return resault

#view_list(column_header())
#view_all_list(list_phone)

#db.write_element('a', add_record_in_list(), name_file) # добавление записи

#delete_record_in_list(list_phone,'Бортник')

editing_record_in_list(list_phone,'Бортник')

#view_list(get_all_element_list(list_phone))    ?

#get_element_list(list_phone,0)
#get_all_element_list(list_phone)
#print(find_word_in_list(list_phone,'Maxim'))