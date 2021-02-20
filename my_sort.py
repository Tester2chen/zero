# 快速排序

def my_sorted(my_list):
    # 1. 設立一个中间值

    middle_num = my_list[0]
    left_list = []
    right_list = []
    for i in my_list:
        # 2. 如果i>中间值，放数组左边，则放右边
        if i >= middle_num:
            left_list.append(i)
        else:
            right_list.append(i)
    my_list = left_list + [my_list[0]] + right_list




