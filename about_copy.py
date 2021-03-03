# 变量赋值过程:
# 对于 x = [1,2,3,4]   
# 首先把1，2，3，4这四个对象在内存中依次创建出来，1,2,3,4这都是字值 对于变量x其实就好像c语言中的指针一样，变量实际上是不存储数据的,他只是绑定数据，
# 列表的赋值实际上就是实现列表与数据的绑定我们在del(x)时并不是删除处列表而是删除的变量x,此时此时列表与变量x没有的绑定关系，python的自带回收机制就会释放列表所占用的内存空间
# x = y = [1,2,3,4] 这其实就是创建多个变量绑定了列表， 在列表中其实是有一个引用计数的，用来记录绑定改列表的变量个数，当该计数为0时也就意味着该列表要被回收了
# 我们再来说说在列表内部机制吧，对于列表的每一个元素都是一个对象，而每一个下标即 x[<index>]就是一个变量然后绑定对应的元素，而我们在改变某一个元素值的时候其实就是该x[<index>]变量绑定另外一个对象 。
# 然后之前的对象没有了绑定他的变量就会被回收机制释放内存 。

# 直接赋值：其实就是对象的引用（别名）。
#
# 浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。
#
# 深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。

# import copy
#
#
# list_a = [5, 7, [2, 8, 5, 4, 9]]
# print("list_a:{0}".format(list_a))
# print("list_a_id:{0}\n".format(id(list_a)))
#
# # 赋值
# list_b = list_a
# print("list_b:{0}".format(list_b))
# print("list_b_id:{0}\n".format(id(list_b)))
#
# list_c = list_a[:]
# print("list_c:{0}".format(list_c))
# print("list_c_id:{0}\n".format(id(list_c)))
#
# # 浅拷贝
# list_d = list_a.copy()
# print("list_d:{0}".format(list_d))
# print("list_d_id:{0}\n".format(id(list_d)))
#
# # 深拷贝
# list_e = copy.deepcopy(list_a)
# print("list_e:{0}".format(list_e))
# print("list_e_id:{0}\n".format(id(list_e)))
#
#
# list_a[2].append("add")
# list_a.append(10)
# list_a[1] = 1
# list_b.append(11)
#
# print("改变分界线================================")
#
# print("list_a:{0}".format(list_a))
# print("list_a_id:{0}\n".format(id(list_a)))
#
#
# # 赋值
#
# print("list_b:{0}".format(list_b))
# print("list_b_id:{0}\n".format(id(list_b)))
#
# print("list_c:{0}".format(list_c))
# print("list_c_id:{0}\n".format(id(list_c)))
#
# # 浅拷贝
#
# print("list_d:{0}".format(list_d))
# print("list_d_id:{0}\n".format(id(list_d)))
#
# # 深拷贝
#
# print("list_e:{0}".format(list_e))
# print("list_e_id:{0}\n".format(id(list_e)))
#
#
# 另一个备注
# a = (1, 5, [3, 2, 8])
# print("a:{0}".format(a))
# print("a:{0}\n".format(id(a)))
# print("a[2]:{0}\n".format(id(a[2])))
#
# a[2].append(10)
# # a[1] = 11
# print("a:{0}".format(a))
# print("a:{0}\n".format(id(a)))
# print("a[2]:{0}\n".format(id(a[2])))

a = [1, 5, [3, 2, 8]]
print("a:{0}".format(a))
print("a:{0}\n".format(id(a)))
print("a[2]:{0}\n".format(id(a[2])))

a[2].append(10)
# a[1] = 11
print("a:{0}".format(a))
print("a:{0}\n".format(id(a)))
print("a[2]:{0}\n".format(id(a[2])))


