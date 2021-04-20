"""
    @author: Spycsh
"""
# You can use create a Python unittest file with
# right click -> New Python file -> Python unit test
# to create a file like this one

import unittest

# call and test the function in src folder
from src import Demo


class TestDemo(unittest.TestCase):
    """Description of your test cases"""

    def test_success(self):
        """test successfully"""
        self.assertEqual(2 + 3, 5)

    @unittest.skip("skip case")
    def test_skip(self):
        pass

    def test_fail(self):
        self.assertEqual(5, 6)

    def test_error(self):
        self.assertEqual(a, 6)


class TestDemo2(unittest.TestCase):

    def test_insert_sort(self):
        self.assertEqual(Demo.insert_sort([4, 2, 3, 1, 5]), [1, 2, 3, 4, 5])

    def test_insert_sort_wrong(self):
        self.assertEqual(Demo.insert_sort_wrong([4, 2, 3, 1, 5]), [1, 2, 3, 4, 5])


# if __name__ == '__main__':
#     suit = unittest.TestSuite()
#     suit.addTest(TestDemo("test_success"))
#     suit.addTest(TestDemo("test_skip"))
#     suit.addTest(TestDemo("test_fail"))
#     suit.addTest(TestDemo2("test_insert_sort"))
#     suit.addTest(TestDemo2("test_insert_sort_wrong"))
#
#     report = "./result.html"
#     with(open(report, 'wb')) as fp:
#         runner = HTMLTestRunner(
#             stream=fp,
#             title='Unit Test report',
#             description='unit test'
#         )
#         runner.run(suit)

    # smtp = SMTP(user="user@126.com", password="123", host="smtp.126.com")
    # smtp.sender(to="user@126.com", attachments=report)
