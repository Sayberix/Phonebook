import data_base as db

name_file = '/db/db'

list_phone = []
list_phone2 = []
list_phone = db.read_element(name_file)
list_phone2 = list_phone[0].split(';')
print(list_phone)
print(list_phone2)