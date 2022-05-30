"""
描述
输入一个正整数，计算它在二进制下的1的个数。
注意多组输入输出！！！！！！

数据范围： 1 <= n <= 2**31 - 1

输入描述：
输入一个整数

输出描述：
计算整数二进制中1的个数
"""

while True:
    try:
        n = int(input())
        print(bin(n).count("1"))
    except:
        break
