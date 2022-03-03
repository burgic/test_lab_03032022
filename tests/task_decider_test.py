import unittest
from src.task_decider import *

class TestTask_Decider(unittest.TestCase):
    def setUp(self):
        self.task_1 = "Wash Dishes"
        self.task_2 = "Cook Dinner"
        self.task_3 = "Clean Windows"
    
    def test_if_task_1_is_passed_through(self):
        get_preferred_option(self.task_1, self.task_2)
        self.assertEqual("Wash Dishes", self.task_1)