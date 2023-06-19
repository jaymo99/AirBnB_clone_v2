#!/usr/bin/python3

import os
import shutil
import unittest
from unittest.mock import patch
from io import StringIO

from console import HBNBCommand
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestConsole(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if os.path.exists("file.json"):
            shutil.copy2("file.json", "backup.json")

    @classmethod
    def tearDownClass(cls):
        if os.path.exists("file.json"):
            pass
            os.remove("file.json")
        if os.path.exists("backup.json"):
            shutil.move("backup.json", "file.json")

    def test_do_create(self):
        createState = 'create State name="California"'
        createPlace = '''create Place city_id="0001" user_id="0001" \
                name="My_little_house" number_rooms=4 number_bathrooms=2 \
                max_guest=10 price_by_night=300 latitude=37.773972 \
                longitude=-122.431297'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(createState)
            output = f.getvalue().strip()
            obj_key = f'State.{output}'

            self.assertIn(obj_key, storage._FileStorage__objects)
            state = storage._FileStorage__objects[obj_key]
            self.assertIsInstance(state, State)
            self.assertTrue(issubclass(State, BaseModel))
            self.assertTrue(hasattr(state, "name"))
            self.assertIsInstance(state.name, str)
            self.assertEqual(state.name, "California")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(createPlace)
            output = f.getvalue().strip()
            obj_key = f'Place.{output}'

            self.assertIn(obj_key, storage._FileStorage__objects)
            place = storage._FileStorage__objects[obj_key]
            self.assertIsInstance(place, Place)
            self.assertTrue(issubclass(Place, BaseModel))
            self.assertTrue(hasattr(place, "city_id"))
            self.assertIsInstance(place.city_id, str)
            self.assertEqual(place.city_id, "0001")
            self.assertTrue(hasattr(place, "user_id"))
            self.assertIsInstance(place.user_id, str)
            self.assertEqual(place.user_id, "0001")
            self.assertTrue(hasattr(place, "name"))
            self.assertIsInstance(place.name, str)
            self.assertEqual(place.name, "My little house")
            self.assertTrue(hasattr(place, "number_rooms"))
            self.assertIsInstance(place.number_rooms, int)
            self.assertEqual(place.number_rooms, 4)
            self.assertTrue(hasattr(place, "number_bathrooms"))
            self.assertIsInstance(place.number_bathrooms, int)
            self.assertEqual(place.number_bathrooms, 2)
            self.assertTrue(hasattr(place, "max_guest"))
            self.assertIsInstance(place.max_guest, int)
            self.assertEqual(place.max_guest, 10)
            self.assertTrue(hasattr(place, "price_by_night"))
            self.assertIsInstance(place.price_by_night, int)
            self.assertEqual(place.price_by_night, 300)
            self.assertTrue(hasattr(place, "latitude"))
            self.assertIsInstance(place.latitude, float)
            self.assertEqual(place.latitude, 37.773972)
            self.assertTrue(hasattr(place, "longitude"))
            self.assertIsInstance(place.longitude, float)
            self.assertEqual(place.longitude, -122.431297)
