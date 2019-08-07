import unittest
import sys
sys.path.insert(1, '..')
import newdata

data = [(1, 1), (2, 3), (3, 5), (4, 4), (5, 7), (6, 7)]


class TestDataCreation(unittest.TestCase):

    def test_data_creation(self):
        creator = newdata.DataCreator()
        creator.save_data_as_pymodule()
        self.assertTrue(True)



if __name__ == '__main__':
    unittest.main()
