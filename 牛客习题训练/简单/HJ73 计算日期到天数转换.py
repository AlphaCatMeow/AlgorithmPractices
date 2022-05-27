# 描述
# 根据输入的日期，计算是这一年的第几天。
# 保证年份为4位数且日期合法。
# 进阶：时间复杂度：O(n)，空间复杂度：O(1)

# 输入描述：
# 输入一行，每行空格分割，分别是年，月，日

# 输出描述：
# 输出是这一年的第几天

"""
思路：
题目给出我们年、月、日的信息
题目希望我们输出这个年月日对应在该年份中是第几天
"""
# 方法一：调用datetime库
# 实现思路
# datetime库中的strftime方法支持以天数的方式输出
# 其中日期格式化符号%j就是天数表示
# 但是这样输出的结果是从001到366为止的字符串
# 我们还要从左边去掉所有的0才是最终的结果
# 时间复杂度O(1)

# import datetime

# while True:
#     try:
#         y,m,d = map(int, input().split())
#         d = datetime.date(y, m, d)                # 录入日期
#         print(d.strftime("%j").lstrip("0"))       # 指定输出一年内的天数并且去掉左边的0
#     except:
#         break

# 方法二：平闰年区别计算
# 实现思路
# 我们知道闰年的二月份是29天，平年的二月份是28天
# 因此在计算某个日子是多少天的时候，要根据平年闰年的不同进行分类塔伦
# 知道这一点后加和所有的天数即可
# 时间复杂度O(1)
# 题解链接：https://blog.nowcoder.net/n/b1456a7cbab840cda74546d6c537a763?f=comment
while True:
    try:
        y, m, d = map(int, input().split())
        month = [31, 28, 31, 30, 31, 30, 31, 31,30, 31, 30, 31]        # 平年的月份
        if y % 400 == 0 or (y % 100 != 0 and y % 4 == 0):
            month[1] = 29                                              # 闰年的月份
        print(sum(month[:m-1]) + d)                                    # 统计时间
    except:
        break
