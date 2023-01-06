#!/usr/bin/python
 # -*- coding: utf-8 -*-

import sys
import controller as cntrl

def ui():
    print("         Телефонный справочник:")
    print("Режимы работы с телефонным справочником:")
    print("1. Просмотр всего справочника")
    print("2. Поиск по реквизитам")
    print("3. Добавление данных")
    print("4. Редактирование данных")
    print("5. Удаление данных")
    print("6. Выход из справочника")

    n = int(input("Выберите режим работы с телефонным справочником: "))

    match n:
        case 1:
            cntrl.view_all_list()
        case 2:
            cntrl.find_record_in_list()
        case 3:
            cntrl.add_record_in_list()
        case 4:
            cntrl.editing_record_in_list()
        case 5:
            cntrl.delete_record_in_list()
        case 6:
            sys.exit()
        case _:
            ui()
