# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

# 22  1221

def my_find(my_list):
    for i in range(0, len(my_list)):
        if my_list[i] == my_list[len(my_list)-i-1]:
            return my_list
        else:
            return False


if __name__ == '__main__':
    result = my_find([1, 2, 2, 1])

    print(result)
