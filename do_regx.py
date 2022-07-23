# -*- coding:utf-8 -*-
'''
@ File: do_regx.py
@ DATE:2022/7/23
@ Author: chenyuanyuan
@ version: python 3
'''
import re
from get_data import GetData

# s = "www.lemfix.com"
# print(re.match("www", s))     # 全匹配 头部匹配
# print(re.match("wwww", s))
# print(re.match("(w)(ww)", s).group(2))  # group 分组，根据你正则表达式里面的括号去分组
# # group()=group(0) 拿到匹配的全字符

# s1 = "hellochenyuanyuantest0001"
# print(re.findall("chenyuanyuan",s1))
# print(re.findall("(chen)(yuan)(yuan)",s1))  # 列表，在字符串里面找匹配的内容，存在列表里面
# # 如果有分组，就是以元祖的形式表现出来，列表嵌套元祖

# s2 = '{"mobile_phone":"${normal_tel}","pwd":"123456"}'
# print(re.search('\$\{(.*)\}',s2).group())
# print(re.search('"\$\{(.*)\}\"',s2).group())
# print(re.search('\$\{(.*?)\}',s2).group())
# print(re.search('\$\{(.*?)\}',s2).group(0))
# print(re.search('\$\{(.*?)\}',s2).group(1))

# s3 = '{"mobile_phone":"${normal_tel}","pwd":"123456"}'
# res = re.search('\$\{(.*?)\}',s3)
# print(res)
# key = res.group(0)
# value = res.group(1)
# new_s = s3.replace(key, str(getattr(GetData, value)))
# print(key, value)
# print(new_s)

class DoRegx():
    def do_regx(self, s):
        while re.search('\$\{(.*?)\}', s):
            key = re.search('\$\{(.*?)\}', s).group(0)
            value = re.search('\$\{(.*?)\}',s).group(1)
            s = s.replace(key, str(getattr(GetData, value)))
        return s


if __name__ == "__main__":
    s4 = '{"mobile_phone":"${normal_tel}","pwd":"${pwd}","cookie":"${cookie}"}'
    print(DoRegx().do_regx(s4))
    print("部署到jenkins成功！！！")