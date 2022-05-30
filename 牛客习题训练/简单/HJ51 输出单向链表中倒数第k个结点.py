"""
描述
输入一个单向链表，输出该链表中倒数第k个结点，链表的倒数第1个结点为链表的尾指针。

链表结点定义如下：
struct ListNode
{
    int m_nKey;
    ListNode* m_pNext;
};
正常返回倒数第k个结点指针，异常返回空指针.

要求：
(1)正序构建链表;
(2)构建后要忘记链表长度。
数据范围：链表长度满足 1 ≤ n ≤ 1000，k ≤ n，链表中数据满足 0 ≤ val ≤ 10000
本题有多组样例输入。

输入描述：
输入说明
1 输入链表结点个数
2 输入链表的值
3 输入k的值

输出描述：
输出一个整数
"""

# 思路：
# 因为华为认为倒数0节点上是没有值的，所以注意处理k是0的情况
# 无脑list，纯考试够用
# 解法1：
while True:
    try:
        count, num_list, k = (
            int(input()),
            [int(x) for x in input().split()],
            int(input()),
        )
        print(num_list[-k] if k else 0)
    except EOFError:
        break

# 链表做法，直接逆向遍历
# 解法2：
# class Node(object):
#     def __init__(self, val=0):
#         self.val = val
#         self.next = None


# while True:
#     try:
#         head = Node()
#         count, num_list, k = int(input()), list(
#             map(int, input().split())), int(input())
#         while k:
#             head.next = Node(num_list.pop())
#             head = head.next
#             k -= 1
#         print(head.val)
#     except EOFError:
#         break
