import unittest
import sys
sys.path.insert(1, '..')
import newdata

data = [(1, 1), (2, 3), (3, 5), (4, 4), (5, 7), (6, 7)]


class TestDataCreation(unittest.TestCase):

    def setUp(self):
        self.creator = newdata.DataCreator()

    def test_data_to_pymodule(self):
        self.creator.save_data_as_pymodule()
        self.assertTrue(True)

    def test_data_to_csv(self):
        self.creator.save_data_as_csv()
        self.assertTrue(True)



if __name__ == '__main__':
    unittest.main()
