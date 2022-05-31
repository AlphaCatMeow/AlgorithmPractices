"""
描述
等差数列 2，5，8，11，14......
（从 2 开始的 3 为公差的等差数列）
输出求等差数列前n项和

数据范围：1 ≤ n ≤ 1000

输入描述：
输入一个正整数n。

输出描述：
输出一个相加后的整数。
"""

while True:
    try:
        s = int(input())
        w = 3 * s + 2
        L = range(2, w, 3)
        print(sum(L))
    except:
        break
