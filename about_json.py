# 一、概念理解
#
# 1、json.dumps()和json.loads()是json格式处理函数（可以这么理解，json是字符串）
# 　　(1)json.dumps()函数是将一个Python数据类型字典进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为json格式的字符串）
# 　　(2)json.loads()函数是将json格式数据转换为字典（可以这么理解，json.loads()函数是将json格式的字符串转化为字典）
#
# 2、json.dump()和json.load()主要用来读写json文件函数

import json


# json.dumps()函数的使用，将字典转化为字符串
# dict1 = {"age": "12"}
# json_info = json.dumps(dict1)
# print("dict1的类型：{0}， dict1本身：{1}".format(type(dict1), dict1))
# print("通过json.dumps()函数处理：")
# print("json_info的类型：{0}， json_info本身：{1}".format(type(json_info), json_info))


# json.loads函数的使用，将字符串转化为字典
# json_info = '{"age": "12"}'
# dict1 = json.loads(json_info)
# print("json_info的类型：{0}， json_info本身：{1}".format(type(json_info), json_info))
# print("通过json.loads()函数处理：")
# print("dict1的类型：{0}， dict1本身：{1}".format(type(dict1), dict1))


# json.dump()函数的使用，将json信息写进文件
# json_info = {'age': '12'}
# file = open('1.json', 'w', encoding='utf-8')

# 将字典转化为字符串
# json_str = json.dumps(json_info)
# print(json_str)
# file.write(json_str)

# 等同于这句
# json.dump(json_info, file)


# json.load()函数的使用，将读取json信息
# file = open('1.json', 'r', encoding='utf-8')
# info = json.load(file)
# print(info)

# 备注
# 1. response.json()的作用就是将API页面的json转化为字典
# 2. response.json（）和json.loads(response.content)都可以将统一编码转化为python类型
# 3. json 语法规定 数组或对象之中的字符串必须使用双引号，不能使用单引号
# exp：
# user_info = "{'name' : 'john', 'gender' : 'male', 'age': 28}"
# 由于字符串使用单引号，会导致运行出错
# user_dict = json.loads(user_info)  失败

# user_info= '{"name" : "john", "gender" : "male", "age": 28}'
# user_dict = json.loads(user_info)  成功

# eval()可以解决以上问题
# user_info = '{"name" : "john", "gender" : "male", "age": 28}'
# user_dict = eval(user_info) 成功
#
# user_info = "{'name' : 'john', 'gender' : 'male', 'age': 28}"
# user_dict = eval(user_info)  成功

# 但是eval()存在安全性问题
# 见 about_eval

# xx.literal_eval()进行转换既不存在使用json进行转换的问题，也不存在使用eval进行转换的安全性问题，因此推荐使用xx.literal_eval()

