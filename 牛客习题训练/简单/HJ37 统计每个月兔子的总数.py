# 描述
# 有一种兔子，从出生后第3个月起每个月都生一只兔子，小兔子长到第三个月后每个月又生一只兔子。
# 例子：假设一只兔子第3个月出生，那么它第5个月开始会每个月生一只兔子。
# 一月的时候有一只兔子，假如兔子都不死，问第n个月的兔子总数为多少？
# 数据范围：输入满足 1 <= n <= 31

# 输入描述：
# 输入一个int型整数表示第n个月

# 输出描述：
# 输出对应的兔子总数

# 思路：
# 本来想用递归算法，但本人不太擅长递归编程，所以总结出简单的逻辑规律，用简单的方式循环迭代。附python代码，以下文字为变量的含义，具体思路看代码
# 归纳：所有兔子就三种,每个月更新三种的数量，迭代完全部相加即为所有兔子数量
# k3-第三个月及以上，可生育
# k2-第二个月，不可生育
# k1-第一个月，小萌新
# 解法：
# import sys
# for s in sys.stdin:
#     m = int(s)
#     k3 = 0
#     k2 = 0
#     k1 = 0
#     for i in range(m):
#         k3 = k3 + k2
#         k2 = k1
#         if k3==0 and k2 == 0:
#             k1 = 1
#         elif k3==0 and k2 == 1:
#             k1 = 0
#         else:
#             k1 = k3
#     print(k1+k2+k3)

# 思路2：斐波那契数列：1 1 2 3 5 8 13 21 34 f(n)=f(n-1)+f(n-2) n>2,n从0开始
# 解法1：递归法
while True:
    try:
        month = int(input())
        n = month-1

        def func(n):
            if n < 2:  # 基线条件
                return 1
            else:  # 递归条件
                return func(n-1)+func(n-2)
        print(func(n))
    except:
        break

# 解法2：循环列表法
# import sys
# for s in sys.stdin:#s=input()读入数据的1行
#     month=int(s)
#     L=[]
#     for i in range(month):
#         if i<2:#前两个月都为1
#             total=1
#             L.append(total)
#         else:
#             total=L[i-1]+L[i-2]#之后均为前两个数的和
#             L.append(total)
#     print(L[-1])#最后的列表L=[1, 1, 2, 3, 5, 8, 13, 21, 34]
