#!/usr/bin/python3
import unittest
import os
from models.user import User
from models.engine.file_storage import FileStorage

class TestUser(unittest.TestCase):
    """Test the User class"""

    def setUp(self):
        """Set up for test"""
        self.user = User()
        self.user.email = "test@mail.com"
        self.user.password = "password"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

    def tearDown(self):
        """Clean up after each test"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_attributes(self):
        """Test the User attributes"""
        self.assertEqual(self.user.email, "test@mail.com")
        self.assertEqual(self.user.password, "password")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_save_reload(self):
        """Test save and reload"""
        FileStorage().save()
        objs = FileStorage().all()
        self.assertEqual(len(objs), 1)
        key = "User." + self.user.id
        self.assertIn(key, objs)
        user_copy = objs[key]
        self.assertEqual(user_copy.id, self.user.id)
        self.assertEqual(user_copy.email, self.user.email)
        self.assertEqual(user_copy.password, self.user.password)
        self.assertEqual(user_copy.first_name, self.user.first_name)
        self.assertEqual(user_copy.last_name, self.user.last_name)

if __name__ == '__main__':
    unittest.main()
