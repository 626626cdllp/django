from django.test import TestCase

from app1.DAO import Chat_MessageDAO
from app1.models import Chat_Message
from app1.test_chat_message import TestChat_Message
import unittest

if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(TestChat_Message("test_chat_message_add"))  # 直接用addTest方法添加单个TestCase
    # 用addTests + TestLoader。不过用TestLoader的方法是无法对case进行排序的
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!__________________________________________________-')
    #将测试结果输出到测试报告中
    with open('C:/Users/cdl/Desktop/UnittestTextReport.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)

