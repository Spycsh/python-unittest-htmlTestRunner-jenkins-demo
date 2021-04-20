"""
    @author: Spycsh
"""

# Here you can create the test suite, call the unit test
# generate the test report, and also send the result to email
import unittest
from TestRunner import HTMLTestRunner
from TestRunner import SMTP
from test import TestDemo, TestDemo2

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestDemo("test_success"))
    suit.addTest(TestDemo("test_skip"))
    suit.addTest(TestDemo("test_fail"))
    suit.addTest(TestDemo("test_error"))
    suit.addTest(TestDemo2("test_insert_sort"))
    suit.addTest(TestDemo2("test_insert_sort_wrong"))

    report = "./result.html"
    with(open(report, 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='Unit Test report',
            description='unit test'
        )
        runner.run(suit)

    # use gmail to provide email sending service
    # smtp = SMTP(user="sender@gmail.com", password="", host="smtp.gmail.com")
    # fill in the receiver email here
    # smtp.sender(to="sihanc@kth.se", attachments=report)