"""
描述
题目标题：
将两个整型数组按照升序合并，并且过滤掉重复数组元素。
输出时相邻两数之间没有空格。

输入描述：
输入说明，按下列顺序输入：
1 输入第一个数组的个数
2 输入第一个数组的数值
3 输入第二个数组的个数
4 输入第二个数组的数值

输出描述：
输出合并之后的数组
"""

# 解法1：
# while true:
#     try:
#         s0,s1,s3,s2 = input(), input().split(), input(), input().split()
#         s = map(str,sorted(map(int, set(s1+s2))))
#         print(''.join(s))
#     except:
#         break

"""
思路：
step1:输入第一个数组的个数、输入第一个数组的数值、输入第二个数组的个数、输入第二个数组的数值；将两个数组的数值合并；创建一个空列表，便于存放整合后的数；
step2:遍历新数组，如果不在空列表中，则添加进去，并将空列表排序；
step3:遍历空列表，逐个打印
"""
# 解法2：
n1 = int(input())
nums1 = list(map(int, input().split()))
n2 = int(input())
nums2 = list(map(int, input().split()))
nums = nums1 + nums2
c = []
for i in nums:
    if i not in c:
        c.append(i)
c.sort()
for i in c:
    print(i, end="")
