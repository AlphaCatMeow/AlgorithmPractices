"""
描述
正整数A和正整数B 的最小公倍数是指 能被A和B整除的最小的正整数值，设计一个算法，求输入A和B的最小公倍数。

数据范围： 1 ≤ a,b ≤ 100000 

输入描述：
输入两个正整数A和B。

输出描述：
输出A和B的最小公倍数。
"""

while True:
    try:
        a, b = list(map(int, input().split()))
        if a < b:
            a, b = b, a
        for i in range(a, a * b + 1, a):
            if i % b == 0:
                print(i)
                break
    except:
        break
