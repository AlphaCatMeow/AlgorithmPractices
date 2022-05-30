"""
描述
Lily上课时使用字母数字图片教小朋友们学习英语单词，每次都需要把这些图片按照大小（ASCII码值从小到大）排列收好。请大家给Lily帮忙，通过代码解决。
Lily使用的图片使用字符"A"到"Z"、"a"到"z"、"0"到"9"表示。

数据范围：每组输入的字符串长度满足 1 ≤ n ≤ 1000 

输入描述：
一行，一个字符串，字符串中的每个字符表示一张Lily使用的图片。

输出描述：
Lily的所有图片按照从小到大的顺序输出
"""

# while True:
#     try:
#         print(''.join(sorted(input())))
#     except EOFError: break

while True:
    try:
        a = input()
        a = list(a)  # 将字符串放入列表中，每个字符为一项
        for i in range(len(a)):
            a[i] = ord(a[i])  # 先转化为ASCLL码
        a.sort()  # 按照ASCLL排序
        for i in range(len(a)):
            a[i] = chr(a[i])  # 再将每个ASCLL还原为字符
        print("".join(a))  # 按要求输出
    except:
        break

# s = input()
# s_lsit=[] # 这个空列表用于装字符串全部转换后的ASCII码
# for item in s:
#     s_lsit.append(ord(item)) #遍历每一个元素，转换为ASCII码，追加进列表
#     pass
# news_list=sorted(s_lsit) # ACSII码列表排序
# res_list=[]# 这个空列表装排序后各个ASCII码转回字符
# for item in news_list:
#     res_list.append(chr(item))# 遍历每一个ASCII码，转换为字符，追加列表
#     pass
# print("".join(res_list)) # 将列表打印为字符串
# pass
# while True:
#     try:
#         s=str(input())
#         func(s)
#         pass
#     except:
#         break
