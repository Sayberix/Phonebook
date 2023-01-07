#!/usr/bin/env python
# -*- coding: latin-1 -*-

import data_base as db
from datetime import datetime as dt
from time import timezone
from parameters import name_file_log

 # �-��� ����������� ��������� ���� �������, ����� �������� ������� ������������� �������
def log_view_all_record():
    global name_file_log
    data = ''
    time = dt.now().strftime('%H:%M') + ";"
    data = time + " view all records" + "\n"
    db.write_element('a', data, name_file_log)

# �-��� ����������� ���������� ������
def log_add_record(data):
    global name_file_log
    time = dt.now().strftime('%H:%M') + ";"
    data = time + " adding an entry: " + data + "\n"
    db.write_element('a', data, name_file_log)

# �-��� ����������� �������� ������
def log_delete_record(data):
    global name_file_log
    time = dt.now().strftime('%H:%M') + ";"
    data = time + " deleting an entry: " + data + "\n"
    db.write_element('a', data, name_file_log)

# �-��� ����������� �������������� ������
def log_update_record(data):
    global name_file_log
    time = dt.now().strftime('%H:%M') + ";"
    data = time + " record editing: " + data + "\n"
    db.write_element('a', data, name_file_log)