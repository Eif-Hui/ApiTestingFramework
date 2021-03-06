#!/user/bin/env python
#coding=utf-8
'''
@author  : H
#@file   : functions.py  excel函数助手
#@ide    : PyCharm
#@time   : 2020-05-30 15:45:16
'''
import hashlib
import uuid as uid
import string
import random
import datetime
import re
from core.aiding_method import *

def fakerdate(name):
    return method_faker(arg=name)


def varstr():
    return "name11"

def md5(arg):
    '''
    md5加密
    :param arg:目标字符串
    :return: 加密后的字符串
    '''
    hash = hashlib.md5()
    hash.update(arg.encode("utf-8"))
    return hash.hexdigest()

def uuid():
    '''
    生成 UUID
    :return:
    '''
    return uid.uuid1()

def onlyint():
    """
    :return: 根据当前时间生成唯一数
    """
    NewData = '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now())
    soleDate = NewData[4:]
    return soleDate

def randomint(length):
    '''
    生成指定长度随机数字
    :param length:
    :return:
    '''
    s = [str(i) for i in range(10)]
    return ''.join(random.sample(s,length))

def randomstr(length):
    '''
    生成指定长度随机数字和大小写字母组合
    :param length:
    :return:
    '''
    return ''.join(random.sample(string.ascii_letters + string.digits  + string.digits, length))

def randomphonenub():
    """
    :return: 生成随机手机号
    """
    preList = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                "153","155", "156", "157", "158", "159", "186", "187", "188", "199"]
    return random.choice(preList) + "".join(random.choice("0123456789") for i in range(8))

def now(pattern="%Y-%m-%d %H:%M:%S",hours=0):
    '''
    生成当前时间 可格式化和设置时间偏移
    :param pattern: 格式如  %Y-%m-%d %H:%M:%S
    :param hours: 设置小时偏移量  如 hours=1 代表当前时间加一小时，支持负数
    :return:
    '''

    return (datetime.datetime.now() + datetime.timedelta(hours=hours)).strftime(pattern)

def regex(target_str,pattern,index=0):
    '''
    正则匹配
    :param target_str: 目标字符串
    :param parttern: 正则表达式
    :param index: 列表索引
    :return: 所有匹配结果，列表形式
    '''
    results = re.findall(pattern,target_str)
    return results[index] if results != [] else results

