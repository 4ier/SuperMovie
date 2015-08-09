# coding:utf-8

import uuid
import MetaInfo

class MovieInfo(MetaInfo):
    '''Movie information entity.
    
    Table Structure 
    CREATE TABLE movie_info
    (
    MovieID varchar(255),
    MovieName varchar(255),
    Poster varchar(255),
    Description varchar(255),
    Released date,
    PRIMARY KEY( MovieID, MovieName )
    )
    '''
    table_fields_dict = {'MovieID':'', 'MovieName':'', 'Poster':'',
                         'Description':'', 'Released':''}
    table_name = 'movie_info'
    
    def __init__(self, movie_name, poster):
        self.table_fields_dict['MovieID'] = uuid.uuid3(uuid.NAMESPACE_DNS, movie_name)
        self.table_fields_dict['MovieName'] = movie_name
        self.table_fields_dict['Poster'] = poster

    def save2DB(self):
        pass
