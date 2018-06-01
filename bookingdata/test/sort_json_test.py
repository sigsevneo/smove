import unittest
import os
# import sort_json


class SortJsonTest(unittest.TestCase):
    def setUp(self):
        print("Setup was done")
        pass

    def tearDown(self):
        print("Tear down was done")
        pass

    def test_A(self):
        print("Test A")

    def test_B(self):
        print("Test B")


if __name__ == '__main__':
    print("Current path is:" + os.path.dirname(__file__))
    unittest.main()
