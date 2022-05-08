# 描述
# 输入一个字符串和一个整数 k ，截取字符串的前k个字符并输出

# 数据范围：字符串长度满足 1 <= n <= 1000 ， 1 <= k <= n
# 输入描述：
# 1.输入待截取的字符串

# 2.输入一个正整数k，代表截取的长度

# 输出描述：
# 截取后的字符串
input_str,k = input(),int(input())
str_length = len(input_str)
if input_str != "":
    if (1 <= k <= str_length):
        print(input_str[0:k])
    else:
        print("输入的整数不在正确范围内")
else:
    print("输入的字符串不符合要求")
