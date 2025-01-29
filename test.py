import unittest
from main import ost

class TestMath(unittest.TestCase):
    def test_ost(self):
        self.assertEqual(ost(5, 3), 2)
        self.assertEqual(ost(100, 3), 1)
        self.assertEqual(ost(800, 50), 0)
        self.assertRaises(ValueError, ost, 10, 0)

if __name__ == "__main__":
    unittest.main()
