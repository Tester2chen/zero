# 一般情况单引号等同于双引号
# eg：
str1 = "hello word"
print(str1)
str2 = 'hello word'
print(str2)


# 在引号内部还需要使用引号

str3 = '"hello word"'
print(str3)
str4 = "'hello word'"
print(str4)
# \将'或者"转义成"和'
str5 = "\"hello,world\""
print(str5)
str6 = '\'hello,world\''
print(str6)
str7 = 'Let\'s go'
print(str7)

# 换行输出
str8 = "c:\nxyy\abc"
print(str8)

# 两个\使\不转义，直接输出字符
str9 = "c:\\nxyy\abc"
print(str9)

# r：不转义，直接输出
str10 = r"c:\nxyy\abc"
print(str10)

# 換行輸出
str11 = """
test
test
"""
print(str11)

