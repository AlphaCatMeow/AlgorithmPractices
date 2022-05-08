# 描述
# 输入整型数组和排序标识，对其元素按照升序或降序进行排序

# 数据范围： 1 <= n <= 1000，元素大小满足 0 <= val <= 100000
# 输入描述：
# 第一行输入数组元素个数
# 第二行输入待排序的数组，每个数用空格隔开
# 第三行输入一个整数0或1。0代表升序排序，1代表降序排序

# 输出描述：
# 输出排好序的数字
import sys
n = int(input().strip())
l = list(map(int, input().strip().split(' ')))
sort_order = int(input().strip())
if 1 <= n <= 1000:
    if len(l) == n:
        for i in l:
            if (i < 0) | (i > 100000):
                print("数组元素大小超出限制范围")
                sys.exit()
        if sort_order == 0:
            l.sort()
        else:
            l.sort(reverse=True)
        for i in l:
            print(i, end=' ')
    else:
        print(f"数组长度不为{n}")
else:
    print("数组长度超出限制范围")
