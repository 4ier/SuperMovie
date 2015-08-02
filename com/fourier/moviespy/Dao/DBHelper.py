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

    def insertMovieInfo(self, movie_info):
        cu = con.cursor()
        cu.execute("""REPLACE INTO movie_info (MovieID, MovieName, Poster, Description, Released) VALUES (?,?,?,?,?)""",
                   (str(movie_info.id), movie_info.name, movie_info.poster, None, None))
        con.commit()

