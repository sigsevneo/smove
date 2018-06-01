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

    def runTest(self):
        # Default test run when Class is called with its constructor
        print("The default test was run.")


if __name__ == '__main__':
    print("Current path is:" + os.path.dirname(__file__))
    unittest.main()
