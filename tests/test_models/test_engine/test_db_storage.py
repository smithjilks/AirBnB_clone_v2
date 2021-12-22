#!/usr/bin/python3
""" Test for db storage"""

import unittest
from models.engine.db_storage import DBStorage
from models import storage
import MySQLdb


class TestDBStorage(unittest.TestCase):
    """ Tests for class attributes and methods
    """


    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "This test is only for database storage.")
    def setUp(self):
        """Set up for test """
        if getenv(HBNB_TYPE_STORAGE) == "db":
            self.my_db = MySQLdb.connect(getenv("HBNB_MYSQL_HOST"),
                                         getenv("HBNB_MYSQL_USER"),
                                         getenv("HBNB_MYSQL_PWD"),
                                         getenv("HBNB_MYSQL_DB"))

            self.cursor = self.my_db.cursor()

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "This test only applies to database storage")
    def tearDown(self):
        """ Close session"""
        if getenv(HBNB_TYPE_STORAGE) == "db":
            self.my_db.close()

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "This test only applies to database storage")
    def test_DBStorage_attributes(self):
        """Tests for class attributes"""

        self.assertTrue(hasattr(DBStorage, '__engine'))
        self.assertTrue(hasattr(DBStorage, '_DBStorage__session'))
        self.assertTrue(hasattr(DBStorage, 'all'))
        self.assertTrue(hasattr(DBStorage, 'new'))
        self.assertTrue(hasattr(DBStorage, 'save'))
        self.assertTrue(hasattr(DBStorage, 'delete'))
        self.assertTrue(hasattr(DBStorage, 'reload'))
