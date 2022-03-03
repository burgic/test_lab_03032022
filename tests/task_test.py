# task_test.py

import unittest
from src.task import Task

class TestTasks(unittest.TestCase):
    def setUp(self):
        self.task = Task("Wash Clothes" , 60)
    
    def test_does_test_have_decription(self):
        self.assertEqual("Wash Clothes",self.task.description)

    def test_does_test_have_duration(self):
        self.assertEqual(60,self.task.duration)
        
        
        
    