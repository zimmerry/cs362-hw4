import unittest
import int_list

class TestAvg(unittest.TestCase):
    def test1(self):
        self.assertEqual(int_list.average([5, 3, 7, 9, 5]), 5.8)

    def test2(self):
        self.assertEqual(int_list.average([6, 2, 7, -1, 8, -10]), 2)

    def test3(self):
        self.assertEqual(int_list.average([]), 0)

if __name__ == '__main__':
    unittest.main()
