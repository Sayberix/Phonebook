#!/usr/bin/python
 # -*- coding: utf-8 -*-

import data_base as db
from parameters import name_file

list_phone = []
list_phone = db.read_element(name_file)

def get_element_list(list_phone: list, position: int) -> list:
    return list_phone[0].split(';')

print(list_phone)
print(list_phone2)