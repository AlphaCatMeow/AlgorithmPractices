"""
描述
有一个m*n大小的数据表，你会依次进行以下5种操作：
1.输入m和n ，初始化m*n大小的表格。
2.输入x1,y1,x2,y2，交换坐标在（x1,y1）和（x2,y2）的两个数。
3.输入x，在第x行上方添加一行。
4.输入y，在第y列左边添加一列。
5.输入x、y，查找坐标为(x,y)的单元格的值。
请编写程序，判断对表格的各种操作是否合法。

详细要求:
1.数据表的最大规格为9行*9列，对表格进行操作时遇到超出规格应该返回错误。
2.对于插入操作，如果插入后行数或列数超过9了则应返回错误。如果插入成功了则将数据表恢复至初始化的m*n大小，多出的数据则应舍弃。
3.所有输入坐标操作，对m*n大小的表格，行号坐标只允许0~m-1，列号坐标只允许0~n-1。超出范围应该返回错误。

本题含有多组样例输入！行列从0开始标号
数据范围：数据组数：1 ≤ t ≤ 5 
进阶：时间复杂度：O(1)，空间复杂度：O(1)

输入描述：
输入数据按下列顺序输入：
1 表格的行列值
2 要交换的两个单元格的行列值
3 输入要插入的行的数值
4 输入要插入的列的数值
5 输入要查询的单元格的坐标

输出描述：
输出按下列顺序输出：
1 初始化表格是否成功，若成功则返回0， 否则返回-1
2 输出交换单元格是否成功
3 输出插入行是否成功
4 输出插入列是否成功
5 输出查询单元格数据是否成功
"""

# 思路：这道题的本质就是数与数之间比大小， 只不过外面套了一个所谓的包装辅以大量的描述来干扰你。 这道题其实就是输入5次数据，然后比5次大小而已。

# # 解法1：
# def create_table(x, y):
#     if 0 < x <= 9 and 0 < y <= 9:
#         global mytable
#         mytable = [[i + j for j in range(y)] for i in range(x)]
#         print("0")
#     else:
#         print("-1")


# def func(x, a):
#     return True if x in range(a) else False


# def exchange_value(x1, y1, x2, y2):
#     if all(map(func, [x1, x2], [a, a])) and all(map(func, [y1, y2], [b, b])):
#         mytable[x1][y1], mytable[x2][y2] = mytable[x2][y2], mytable[x1][y1]
#         print("0")
#     else:
#         print("-1")


# def add_row(x):
#     if func(x, a) and a + 1 <= 9:
#         mytable.insert(x - 1, [j for j in range(b)])
#         mytable.pop()
#         print("0")
#     else:
#         print("-1")


# def add_colomn(y):
#     if func(y, b) and b + 1 <= 9:
#         for i in range(a):
#             mytable[i].insert(y - 1, i)
#             mytable[i].pop()
#         print("0")
#     else:
#         print("-1")


# def check_cell(x, y):
#     if func(x, a) and func(y, b):
#         print("0")
#     else:
#         print("-1")


# while True:
#     try:
#         a, b = map(int, input().split())
#         create_table(a, b)
#         c, d, e, f = map(int, input().split())
#         exchange_value(c, d, e, f)
#         g = int(input())
#         add_row(g)
#         h = int(input())
#         add_colomn(h)
#         k, l = map(int, input().split())
#         check_cell(k, l)
#     except:
#         break

# # 解法2：
while True:
    try:
        m, n = map(int, input().split())
        x1, y1, x2, y2 = map(int, input().split())
        x, y = int(input()), int(input())
        x3, y3 = map(int, input().split())
        print(0 if m <= 9 and n <= 9 else -1)
        print(0 if x1 < m and x2 < m and y1 < n and y2 < n else -1)
        print(0 if 9 > m > x else -1)
        print(0 if 9 > n > y else -1)
        print(0 if x3 < m and y3 < n else -1)
    except:
        break
