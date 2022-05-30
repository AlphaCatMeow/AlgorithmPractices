"""
描述
完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。
它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
例如：28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。
输入n，请输出n以内(含n)完全数的个数。

数据范围： 1 <= n <= 5 * 10**5

输入描述：
输入一个数字n

输出描述：
输出不超过n的完全数的个数

思路：
1. 定义一个真因子列表的方法
2. 用循环判断约数和是否等于本身
"""

# 解法：
def factorlist(num):
    if num == 1:
        return False
    list = []
    for i in range(1, num):
        if num % i == 0:
            list.append(i)
    return list


while True:
    try:
        n = int(input())
        count = 0
        for j in range(2, n + 1):
            m = sum(factorlist(j))
            if m == j:
                count += 1
        print(count)
    except:
        break
