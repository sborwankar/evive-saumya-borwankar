import unittest
from menu import OrderList
# USAGE: python3 -m unittest test.py
class TestMenu(unittest.TestCase):
    orderClass=OrderList()
    def test_orderList_breakfast1(self):
        actual = self.orderClass.orderList(inputString="Breakfast 1,2,3")
        expected = "Eggs, Toast, Coffee"
        self.assertEqual(actual, expected)

    def test_orderList_breakfast2(self):
        actual = self.orderClass.orderList(inputString="Breakfast 2,3,1")
        expected = "Eggs, Toast, Coffee"
        self.assertEqual(actual, expected)

    def test_orderList_breakfast3(self):
        actual = self.orderClass.orderList(inputString="Breakfast 1,2,3,3,3")
        expected = "Eggs, Toast, Coffee(3)"
        self.assertEqual(actual, expected)

    def test_orderList_breakfast4(self):
        actual = self.orderClass.orderList(inputString="Breakfast 1")
        expected = "Unable to process: Side is missing"
        self.assertEqual(actual, expected)

    def test_orderList_lunch1(self):
        actual = self.orderClass.orderList(inputString="Lunch 1,2,3")
        expected = "Sandwich, Chips, Soda"
        self.assertEqual(actual, expected)

    def test_orderList_lunch2(self):
        actual = self.orderClass.orderList(inputString="Lunch 1,2")
        expected = "Sandwich, Chips, Water"
        self.assertEqual(actual, expected)

    def test_orderList_lunch3(self):
        actual = self.orderClass.orderList(inputString="Lunch 1,1,2,3")
        expected = "Unable to process: Sandwich cannot be ordered more than once"
        self.assertEqual(actual, expected)
    def test_orderList_breakfast5(self):
        actual = self.orderClass.orderList(inputString="Breakfast 1,2")
        expected = "Eggs, Toast, Water"
        self.assertEqual(actual, expected)

    def test_orderList_lunch4(self):
        actual = self.orderClass.orderList(inputString="Lunch 1,2,2")
        expected = "Sandwich, Chips(2), Water"
        self.assertEqual(actual, expected)

    def test_orderList_dinner1(self):
        actual = self.orderClass.orderList(inputString="Dinner 1,2,3,4")
        expected = "Steak, Potatoes, Wine, Cake, Water"
        self.assertEqual(actual, expected)

    def test_orderList_dinner2(self):
        actual = self.orderClass.orderList(inputString="Dinner 1,2,3,3,4")
        expected = "Unable to process: Wine cannot be ordered more than once"
        self.assertEqual(actual, expected)

    def test_orderList_dinner3(self):
        actual = self.orderClass.orderList(inputString="Dinner 1,2,4")
        expected = "Steak, Potatoes, Cake, Water"
        self.assertEqual(actual, expected)
        
    def test_orderList_dinner4(self):
        actual = self.orderClass.orderList(inputString="Dinner 1,2,4,5")
        expected = "Unable to process: Meal item not on menu / Please type order correctly"
        self.assertEqual(actual, expected)

    def test_orderList_dinner5(self):
        actual = self.orderClass.orderList(inputString="Dinner 1,4")
        expected = "Unable to process: Side is missing"
        self.assertEqual(actual, expected)

    def test_orderList_dinner6(self):
        actual = self.orderClass.orderList(inputString="dinnner 1,3,2,4")
        expected = "Unable to process: Meal type not on menu"
        self.assertEqual(actual, expected)

    def test_orderList_breakfast6(self):
        actual = self.orderClass.orderList(inputString="breakfast 1,2,4")
        expected = "Unable to process: Meal item not on menu / Please type order correctly"
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()