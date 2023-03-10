#!/usr/bin/python
 # -*- coding: utf-8 -*-

import data_base as db
import logger as log
from parameters import name_file_db

def init_db():
    return db.read_element(name_file_db)

# получение записи строки в виде списка (внутренняя ф-ция)
def get_element_list(position_in_list: int) -> list:
    list_phone = init_db()
    return list_phone[position_in_list].split(';')

# представление в удобочитаемой форме
def view_list(list_phone: list) -> str:
    data = ''
    for i in range(len(list_phone)):
        if i < len(list_phone) - 1:
            data += str(list_phone[i]) + ' | '
        else:
            data += str(list_phone[i]) + ' | ' + '\n'
    #[print(list_phone[i], ' | ', end=' ') if i < len(list_phone) - 1 else print(list_phone[i], ' | ', '\n') for i in range(len(list_phone)) ]
    return data

# шапка колонок
def column_header():
    print(view_list(['Фамилия','Имя','Телефон','Описание']))
        
# просмотр всех записей
def view_all_list():
    list_phone = init_db()
    column_header()
    [print(view_list(get_element_list(i))) for i in range(len(list_phone))]
    log.log_view_all_record()

# добавление записей в строку - универсальная ф-ция (для добавления и редактирования)
def add_record_in_list_universal() -> str:
    return str(input('Введите фамилию: ')) + ';' + str(input('Введите имя: ')) + ';' + str(input('Введите телефон: ')) + ';' + str(input('Введите описание: ')) + '\n'

# добавление записей в строку
def add_record_in_list():
    data = add_record_in_list_universal()
    db.write_element('a', data, name_file_db)
    print('Запись добавлена!')
    log.log_add_record(data)

def enter_key_word() -> str:
    return str(input('Введите ключевое слово: '))

# удаление записи по ключевому слову
def delete_record_in_list() -> db.write_element:
    list_phone = init_db()
    key_word = enter_key_word()
    resault = ''
    for i in range(len(list_phone)):
        entry = get_element_list(i)
        for j in entry:
            find_word = False
            if key_word in j:
                find_word = True
                column_header()
                print(view_list(entry))
                for_delete = 'Y'
                for_delete = str(input('Вам нужна эта запись для удаления? (Y/n):'))
                if for_delete == 'Y' or for_delete == "":
                    print("Запись удалена!")
                    log.log_delete_record(view_list(entry))
                    break
        if find_word == False:
            resault += ";".join(entry) + '\n'
    db.write_element('w', resault, name_file_db)

def find_record_in_list():
    list_phone = init_db()
    key_word = enter_key_word()
    resault = ''
    for i in range(len(list_phone)):
        entry = get_element_list(i)
        for j in entry:
            find_word = False
            if key_word in j:
                find_word = True
                column_header()
                print(view_list(entry))
                #break

# редактирование записи по ключевому слову
def editing_record_in_list() -> db.write_element:
    list_phone = init_db()
    key_word = enter_key_word()
    resault = ''
    for i in range(len(list_phone)):
        entry = get_element_list(i)
        for j in entry:
            find_word = False
            if key_word in j:
                find_word = True
                column_header()
                print(view_list(entry))
                for_delete = 'Y'
                for_delete = str(input('Вам нужна эта запись для редактирования? (Y/n):'))
                if for_delete == 'Y' or for_delete == "":
                    resault += add_record_in_list_universal()
                    print("Запись отредактирована!")
                    log.log_update_record(view_list(entry))
                    break
        if find_word == False:
            resault += ";".join(entry) + '\n'
    db.write_element('w', resault, name_file_db)

# поиск слова по всему списку справочника и запись его позиции в список кортежей
#def find_word_in_list(key_word = enter_key_word()) -> list[tuple]:
#    list_phone = init_db()
#    resault = []
#    for i in range(len(list_phone)):
#        entry = get_element_list(list_phone,i)
#        for j in range(len(entry)):
#            if entry[j] == key_word:
#                tuple_rec = (i, j)  # где i - это номер строки а j - номер записи в строке
#                resault.append(tuple_rec)
#    return resault

#column_header()
#view_all_list(list_phone)

#db.write_element('a', add_record_in_list(), name_file) # добавление записи

#delete_record_in_list(list_phone,'Бортник')

#editing_record_in_list(list_phone,'Бортник')

#view_list(get_all_element_list(list_phone))    ?

#get_element_list(list_phone,0)
#get_all_element_list(list_phone)
#print(find_word_in_list(list_phone,'Maxim'))