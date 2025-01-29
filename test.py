import unittest
from main import add, subtract, multiply, divide

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(6, 4), 9) # неправильный
        self.assertEqual(add(-2, 3), 1)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(6, 4), 1) # неправильный
        self.assertEqual(subtract(-2, 3), -5)

    def test_multiply(self):
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(6, 4), 20) # неправильный
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(15, 3), 5)
        self.assertEqual(divide(24, 4), 5) # неправильный
        self.assertEqual(divide(10, 0), "Error: Division by zero")

if __name__ == "__main__":
    unittest.main()
