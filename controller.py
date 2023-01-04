#!/usr/bin/python
 # -*- coding: utf-8 -*-

import data_base as db
from parameters import name_file

list_phone = []
list_phone = db.read_element(name_file)     # получаем весь список справочника по строкам
#print(list_phone)

# ф-ция получение записи строки в справочнике
def get_record_list(list_phone: list, position_in_list: int) -> list:
    list_phone2 = []
    list_phone2 = list_phone[position_in_list].split(';')
    return list_phone2

def get_all_records(list_phone: list) -> list:
    for i in range(len(list_phone)):
        print(get_record_list(list_phone,i))

get_all_records(list_phone)
#print(get_record_list(list_phone,0))
#print(get_record_list(list_phone,1))