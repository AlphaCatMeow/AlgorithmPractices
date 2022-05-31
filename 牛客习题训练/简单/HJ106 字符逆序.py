"""
描述
将一个字符串str的内容颠倒过来，并输出。

数据范围：1 ≤ len(str) ≤ 10000 

输入描述：
输入一个字符串，可以有空格

输出描述：
输出逆序的字符串
"""

while True:
    try:
        s = list(input())
        print("".join(s[::-1]))
    except:
        break
