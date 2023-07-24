#!/usr/bin/python3
'''db_storage module
defines database storage engine
'''
from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models.base_model import Base
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    '''Database storage engine'''
    __engine = None
    __session = None

    classes = {
            'State': State,
            'City': City
            # 'Place': Place,
            # 'Review': Review,
            # 'Amenity': Amenity,
            # 'User': User
            }

    def __init__(self):
        '''initializes the database storage engine'''
        try:
            self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                          .format(getenv('HBNB_MYSQL_USER'),
                                                  getenv('HBNB_MYSQL_PWD'),
                                                  getenv('HBNB_MYSQL_HOST'),
                                                  getenv('HBNB_MYSQL_DB')
                                                  ),
                                          pool_pre_ping=True)
        except Exception as e:
            print(f'Exception: {type(e).__name__}')
            print(f'Message: {str(e)}')
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''Query the db all objects depending on the class name.'''
        new_dict = {}
        classes = [cls] if cls is not None else self.classes.values()
        for _cls in classes:
            objs = self.__session.query(_cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        '''add an object to the current db session.'''
        if obj:
            self.__session.add(obj)

    def delete(self, obj=None):
        '''delete an object from the current db session.'''
        if obj:
            self.__session.delete(obj)

    def save(self):
        '''commit all changes of the current db session.'''
        self.__session.commit()

    def reload(self):
        '''creates db tables and current db session.'''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        ScopedSession = scoped_session(session_factory)
        self.__session = ScopedSession()

    def close(self):
        '''closes current session
        '''
        self.__session.close()
