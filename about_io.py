# 1. 时间
# 2. api的名称
# 3. 数字   求第三列的平均值以及中位数
# python之read()
# rf.read()
# 特点：读取整个文件，将文件内容放到一个字符串变量中。
# 缺点：如果文件非常大，尤其是大于内存时，无法使用read（）方法。
# rf.readline()
# 特点：readline()方法每次读取一行；返回的是一个字符串对象，保持当前行的内存
# 缺点：比readlines慢的多
# lineslist = rf.readlines()
# 特点：一次性读取整个文件；自动将文件内容分析成一个行的列表
# from numpy import *
from __future__ import division
import math


def get_num():
    # 1.读取文件
    with open('file1', 'r', encoding='utf-8') as rf:
        # lineslist = rf.read()
        # lineslist = rf.readline()
        lineslist = rf.readlines()
    print(lineslist, type(lineslist))
    numlist = []
    sum_num = 0
    for line in lineslist:
        line = line.strip().split(',')
        # print(line)
        sum_num += float(line[2])
        numlist.append(line[2])
    # print(numlist)
    # print(sum_num)
    avg_num = sum_num/len(numlist)
    print("平均值为:{0}".format(avg_num))
    numlist.sort()
    print(numlist)
    if len(numlist)/2 != 0:
        # 截断小数部分
        # middle_num = numlist[math.trunc(len(numlist)/2)]
        # 向下取整
        middle_num = numlist[len(numlist) // 2]
    else:
        # middle_num = (numlist[math.trunc(len(numlist)/2)] + numlist[math.trunc(len(numlist)/2) + 1])/2
        middle_num = (numlist[len(numlist) // 2] + numlist[len(numlist) // 2 + 1]) / 2
    print("中位数为:{0}".format(middle_num))

# def get_num():
#     # 1.读取文件
#     with open('file1', 'r', encoding='utf-8') as rf:
#         # lineslist = rf.read()
#         numlist = []
#         while True:
#             line = rf.readline()
#             if line:
#                 line = line.strip().split(',')
#                 print(line)
#                 numlist.append(line[2])
#             else:
#                 break
#     print(numlist)


if __name__ == '__main__':
    get_num()
# readlines()  split()

#
# 1. 学生id  学生A
# 2. 课程  语文
# 3. 课程分数 70


# 地点搜索框
