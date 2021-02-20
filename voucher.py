def get_result(num):
    if len(num) == 12:
        num1 = num[0:len(num)-1:2]
        num2 = num[1:len(num):2]
        print(num1, num2)
        sum1 = 0
        sum2 = 0
        for i in num1:
            sum1 = int(i)*1 + sum1
            # print("sum1:", sum1)
        for j in num2:
            sum2 = int(j)*3 + sum2
            # print("sum2:", sum2)
        sum = sum1 + sum2
        print(sum)
    else:
        print("字符串{0}位数为{1}位, 不为12位".format(num, len(num)))


if __name__ == "__main__":
    get_result("600000000038")