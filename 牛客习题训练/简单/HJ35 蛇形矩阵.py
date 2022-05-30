"""
描述
蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。

例如，当输入5时，应该输出的三角形为：
1 3 6 10 15
2 5 9 14
4 8 13
7 12
11

输入描述：
输入正整数N（N不大于100）

输出描述：
输出一个N行的蛇形矩阵。
"""

while True:
    try:
        num = int(input())
        for i in range(num):
            if i == 0:
                res = [(x + 2) * (x + 1) // 2 for x in range(num)]
            else:
                res = [x - 1 for x in res[1:]]
            print(" ".join(map(str, res)))
    except:
        break

"""
另一种思路：
把蛇形矩阵旋转45度其实就是个金字塔，最上面是1，最右下方是最大的数，即10
原本：
1 3 6 10
2 5 9
4 8
7
旋转一下：
1
2 3
4 5 6
7 8 9 10
list1就是旋转后的矩阵
然后可以发现旋转后的矩阵里每一行的最后一个元素，就是蛇形矩阵中第一行的元素，倒数第二个元素就是第二行的，依次类推。
"""

# # 解法：
# while 1:
#     try:
#         n = int(input())
#         list1 = []
#         for i in range(1,n+1):
#             list1.append([0]*i)
#         a = 0
#         for i in range(n):
#             for j in range(i+1):
#                 a = a + 1
#                 list1[i][j]=a
#         list2,she = [],[]
#         for i in range(1,n+1):
#             for line in list1:
#                 if line:
#                     list2.append(line.pop(-1))
#             she.append(" ".join(map(str,list2)))
#             list2 = []
#         for i in she:
#             print(i)
#     except:
#         break
