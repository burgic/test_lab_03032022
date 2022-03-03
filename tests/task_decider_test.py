import unittest
from src.task_decider import *
from src.task import Task

class TestTask_Decider(unittest.TestCase):
    def setUp(self):
        self.task_1 = Task("Wash Dishes", 15)
        self.task_2 = Task("Cook Dinner", 60)
        self.task_3 = Task("Clean Windows", 120)
    
    def test_if_task_1_is_passed_through(self):
        get_preferred_option(self.task_1, self.task_2)
        self.assertEqual("Wash Dishes", self.task_1.description)

    def test_if_wash_over_dinner(self):
        get_preferred_option(self.task_2, self.task_1)
        self.assertEqual("Wash Dishes", self.task_1.description)