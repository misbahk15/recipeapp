import unittest
from datetime import date
from dateutil.relativedelta import relativedelta
import app
class testclass(unittest.TestCase):
    def test_dish_name(self):
        self.assertTrue("dish_name",'tandoori mutton')
    def test_is_vegeterian(self):
        self.assertEqual("is_vegeterian",'True')
    def test_people_count(self):
        self.assertTrue("people_count",2)
    def test_people_count_check(self):
        self.assertEqual("people_count",1)
    def test_is_vegeterian_check(self):
        self.assertTrue("is_vegeterian",'False')
    def test_dish_name_check(self):
        self.assertFalse("dish_name",'tandoori mutton')
    def test_ingredient(self):
        testList = ["mutton","mutton masala"]
        value = ["mutton","mutton masala"]
        self.assertListEqual(testList, value)
    def test_ingredient_check(self):
        testList = ["mutton","mutton masala"]
        value = ["mutton"]
        self.assertListEqual(testList, value)
    def test_dish_recipe(self):
        self.assertTrue("dish_recipe",'marinate and cook')
    def test_dish_recipe_check(self):
        self.assertFalse("dish_recipe",'marinate and cook')


if __name__ == '__main__':
    unittest.main()
