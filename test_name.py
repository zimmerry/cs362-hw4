import unittest
import name

class TestAvg(unittest.TestCase):
    def test1(self):
        self.assertEqual(name.full("John", "Doe"), "John Doe")

    def test2(self):
        self.assertEqual(name.full("Jane", "Doh"), "Jane Doh")

    def test3(self):
        self.assertEqual(name.full("Joshua", "O'Connell"), "Joshua O'Connell")

if __name__ == '__main__':
    unittest.main()
