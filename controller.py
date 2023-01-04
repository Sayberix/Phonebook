#!/usr/bin/python
 # -*- coding: utf-8 -*-

import data_base as db
from parameters import name_file

list_phone = []
list_phone = db.read_element(name_file)

def get_element_list(list_phone_func: list, position: int) -> list:
    return list_phone_func[position].split(';')

def get_all_element_list(list_phone_func: list) -> list:
    for i in range(len(list_phone_func)):
        print(get_element_list(list_phone_func,i))

#get_element_list(list_phone,0)
get_all_element_list(list_phone)