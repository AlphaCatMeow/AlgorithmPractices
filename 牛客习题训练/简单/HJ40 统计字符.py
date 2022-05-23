# 描述
# 输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数。

# 数据范围：输入的字符串长度满足 1 ≤ n ≤ 1000

# 输入描述：
# 输入一行字符串，可以有空格

# 输出描述：
# 统计其中英文字符，空格字符，数字字符，其他字符的个数

# 解法1：
# while True:
#     try:
#         s = input()
#         l = [0, 0, 0]
#         for i in s:
#             l[0] += int(i.isalpha())
#             l[1] += int(i == ' ')
#             l[2] += int(i.isnumeric())
#         print(l[0])
#         print(l[1])
#         print(l[2])
#         print(len(s)-l[0]-l[1]-l[2])
#     except:
#         break

# 解法2：
import re
while True:
    try:
        s = input()
        print(len(''.join(re.findall(r'[a-zA-Z]+', s))))
        print(len(''.join(re.findall(r' ', s))))
        print(len(''.join(re.findall(r'\d', s))))
        print(len(''.join(re.findall(r'[^a-zA-Z0-9 ]+', s))))
    except:
        break
