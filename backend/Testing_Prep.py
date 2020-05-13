#!/usr/bin/env python
# coding: utf-8

# # Testing Prep
# 
# Before you get started writing your own testing code, we'll review the essential elements of writing a test suite using unittest in Python3. 

# In[ ]:


# Import all dependencies
import unittest
import json
from flaskr import create_app
from models import setup_db


# In[ ]:


class ResourceTestCase(unittest.TestCase):
    """This class represents the resource test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "test_db"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
    
    def tearDown(self):
        """Executed after each test"""
        pass

    def test_given_behavior(self):
        """Test _____________ """
        res = self.client().get('/')

        self.assertEqual(res.status_code, 200)


# In[ ]:


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()

