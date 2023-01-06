#!/usr/bin/python
 # -*- coding: utf-8 -*-

import sys
import controller as cntrl

def ui():
    print("         ���������� ����������:")
    print("������ ������ � ���������� ������������:")
    print("1. �������� ����� �����������")
    print("2. ����� �� ����������")
    print("3. ���������� ������")
    print("4. �������������� ������")
    print("5. �������� ������")
    print("6. ����� �� �����������")

    n = int(input("�������� ����� ������ � ���������� ������������: "))

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
