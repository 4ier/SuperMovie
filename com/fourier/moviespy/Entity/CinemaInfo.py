# coding:utf-8

import uuid
import MetaInfo

class CinemaInfo(MetaInfo):
    '''Ciname information entity.
    
    CREATE TABLE cinema_info
    (
    CinemaID varchar(255),
    CinemaName varchar(255),
    Location varchar(255),
    Logo varchar(255), Description, CityID, City,
    PRIMARY KEY( CinemaID, CinemaName )
    );
    '''
    table_fields_dict = {'CinemaID':'', 'CinemaName':'', 'Location':'',
                          'Logo':'', 'Description':'', 'CityID':'', 'City':''}
        
    def __init__(self, cinema_name, location, logo, desc, city=u'深圳'):
        self.table_fields_dict['CinemaID'] = uuid.uuid3(uuid.NAMESPACE_DNS, cinema_name)
        self.table_fields_dict['CinemaName'] = cinema_name
        self.table_fields_dict['Location'] = location
        self.table_fields_dict['Logo'] = logo
        self.table_fields_dict['Description'] = desc
        self.table_fields_dict['CityID'] = uuid.uuid3(uuid.NAMESPACE_DNS, city)
        self.table_fields_dict['City'] = city
