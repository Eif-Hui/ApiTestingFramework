#!/user/bin/env python
#coding=utf-8
'''
@author  : H
#@file   : manage.py
#@ide    : PyCharm
#@time   : 2020-05-28 15:27:00
'''

'''
    pytest用例执行文件
'''
if __name__ == '__main__':
    import pytest
    import time
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    # 并发暂时存在问题
    pytest.main(['-s','./testcase/','--html=report/{}_report.html'.format(now)])


