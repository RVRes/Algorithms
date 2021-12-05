import unittest

from transpond_array import Matrix


class Test_transpond_array(unittest.TestCase):

    def setUp(self):
        self.matrix = Matrix()
        self.matrix.fill_array2(10)

    def test_transpond(self):
        self.assertEqual(self.matrix.transpond_array2()[7][3], self.matrix.get_array()[3][7])
        self.assertIsInstance(self.matrix.transpond_array2(), list)
        self.assertIsInstance(self.matrix.transpond_array2()[0], list)
        self.assertIsInstance(self.matrix.transpond_array2()[0][0], int)
        self.assertFalse(1 > 2)


if __name__ == "__main__":
    unittest.main()
