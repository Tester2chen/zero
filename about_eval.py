# eval是Python的一个内置函数，这个函数的作用是，返回传入字符串的表达式的结果
# 首先是表达式求值运算：
# s='8*8'
# eval(s)   64
# eval('2+5*4')   22
# x=1
# y=4
# eval('x+y')
# eval('98.9')  98.9
# eval('9.9\n')  9.9
# eval('9.9\n\t\r  \t\r\n')  9.9

# 最有用的一个是eval可以将字符串转换成字典，列表，元组
# l = "[2,3,4,5]"
# ll =eval(l)    [2, 3, 4, 5]
# type(ll)    <type 'list'>
# d="{'name':'python','age':20}"
# dd=eval(d)   {'age': 20, 'name': 'python'}
# type(dd)   <type 'dict'>
#
# t='(1,2,3)'
# tt=eval(t)   (1, 2, 3)
# >>> type(tt)   <type 'tuple'>





# eval虽然方便，但是要注意安全性，可以将字符串转成表达式并执行，就可以利用执行系统命令，删除文件等操作。
# 假设用户恶意输入。比如：
# eval("__import__('os').system('ls /Users/chunming.liu/Downloads/')")
# 那么eval()之后，你会发现，当前文件夹文件都会展如今用户前面。这句其实相当于执行了
# os.system('ls /Users/chunming.liu/Downloads/')
# 那么继续输入：
# eval("__import__('os').system('cat /Users/chunming.liu/Downloads/tls_asimov_cert.pem')")
# 代码都给人看了。
# 再来一条删除命令，文件消失。比如
# eval("__import__('os').system('rm /Users/chunming.liu/Downloads/车辆转发测试.png')")
# 所以使用eval，一方面享受他的了灵活性同时，也要注意安全性。