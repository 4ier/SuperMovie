# coding:utf-8
from com.fourier.moviespy.Dao.DBHelper import DBHelper

class MetaInfo(object):
    '''Meta information entity.
    
    Attributes: 
        table_fields_dict: store all table fields.
    
    '''

    table_fields_dict = {}
    table_name = ''
    dbHelper = DBHelper()

    def __init__(self, params):
        pass

    def save2DB(self):
        self.dbHelper.insertMovieInfo(self.table_name, self)
