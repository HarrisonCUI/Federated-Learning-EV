#自动化用户沟通数据分析模块
#用于极视角比赛用户问题分析

# 获得信息数据结构如下 （时间+（用户号）+ 留言信息）:
# 2020-03-31 22:13:38 (331505349)
# 有人在添加 --disable_nhwc_to_nchw 选项后遇到这个问题吗
# 分析思路: 数据呈现分为日，周，月，主要从用户流失，用户问题， 用户活跃度，自动归类用户问题的
# 内容来进行分析 ，目的是基于用户互动数据来进行不同阶段的产品开发决策
# 
#主要涉及第三方模块： MATPLOTLIB ,JIEBA, XLWT

import re
# import xlsxwriter
import matplotlib.pyplot as mlt
import numpy
import jieba 
import pandas
# import xlwt

# 正则匹配数据信息

# 匹配日期
date_re = re.compile(r"^\d{4}-\d{2}-\d{2}$")
# 匹配时间
time_re = re.compile(r"\d{1,2}:\d{2}:\d{2}$")
# 匹配用户名
name_re_num = re.compile(r"\((\d+)\)")
name_re_mail = re.compile(r"\<(.*?@.*?)\>")
# 匹配用户
person_re = re.compile(r"^\S+?\s\d{1,2}:\d{2}:\d{2}$")

#导入QQ群聊数据并转换为Excel或CSV
ChatData = open('./cv.txt','r')

#数据预处理
def read_data():
    text = []
    message = ChatData


#数据分析
def Count_User():
    print('done')


#数据可视化
def DrawGra():
    pass

print(ChatData)
print('Done2')