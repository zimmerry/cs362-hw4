import unittest
import cube

class TestVol(unittest.TestCase):
    def test1(self):
        self.assertEqual(cube.volume(10), 1000)

    def test2(self):
        self.assertEqual(cube.volume(6548), 280754038592)

    def test3(self):
        self.assertEqual(cube.volume(-3), -1)

    def test4(self):
        with self.assertRaises(TypeError):
            cube.volume('asba')

if __name__ == '__main__':
    unittest.main()
