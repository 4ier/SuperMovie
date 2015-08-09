# coding:utf-8

import sqlite3

class DBHelper:

    global DB_PATH
    DB_PATH = 'D:/DOC/DEV/python/SuperMovie/com/fourier/moviespy/DB/test.db'
    global con
    con = sqlite3.connect(DB_PATH)
    con.text_factory = str

    def __init__(self):
        pass

    def insertMovieInfo(self, table_name, meta_info):
        'INSERT INRO ' + table_name + meta_info.table_fields_dict.keys() + meta_info.table_fields_dict.values()
        cu = con.cursor()
        cu.execute(table_name % meta_info.table_fields_dict.keys() % meta_info.table_fields_dict.values())
        con.commit()
