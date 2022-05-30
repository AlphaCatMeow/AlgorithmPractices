"""
描述
求一个int类型数字对应的二进制数字中1的最大连续数，例如3的二进制为00000011，最大连续2个1

数据范围：数据组数：1 ≤ t ≤ 5，1 ≤ n ≤ 500000 
进阶：时间复杂度：O(logn)，空间复杂度：O(1)

输入描述：
输入一个int类型数字

输出描述：
输出转成二进制之后连续1的个数
"""

while True:
    try:
        x = int(input())
        byte_x = bin(x)[2:]
        list1 = sorted(list(set(byte_x.split("0"))), key=lambda x: len(x), reverse=True)
        print(len(list1[0]))
    except:
        break
