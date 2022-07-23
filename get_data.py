# -*- coding:utf-8 -*-
'''
@ File: get_data.py
@ DATE:2022/7/23
@ Author: chenyuanyuan
@ version: python 3
'''
import random, string
class GetData:
    HeadNumList = ["130", "131", "137", "138", "145", "146", "147", "150", "151", "152", "158", "172",
                   "174", "175", "180", "181", "182", "198"]
    EightNum = "".join(random.sample(string.digits, 8))
    mobile = int(random.choice(HeadNumList) + EightNum)
    normal_tel = str(mobile + 1)
    pwd = "qa_"+"test"+str(EightNum)
    cookie = "test-cookie-fedf-4744-a81d811aeb-"+str(EightNum)