"""
描述
给定一个字符串描述的算术表达式，计算出结果值。
输入字符串长度不超过 100 ，合法的字符包括 ”+, -, *, /, (, )” ， ”0-9” 。
数据范围：运算过程中和最终结果均满足 |val| <= 2**31-1 ，即只进行整型运算，确保输入的表达式合法

输入描述：
输入算术表达式

输出描述：
计算出结果值
"""

# # 思路1：
# # 这道题的考察用法应该是用堆栈，因为python3没有栈，所以用list仿造一个堆栈。
# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         return self.items.pop()

#     def peek(self):
#         return self.items[-1]

#     def size(self):
#         return len(self.items)

# # 分割器
# # 本题首先给出一个字符串，所以要定义一个splitter，分割数字和字符。
# # 这里我用的是一个双指针的办法，pre是前一个字符，如果是数字字符，就用0，如果是别的运算字符，就用1。
# # 当发现从数字变成运算符的时候，lst增加整个数字。
# # 当发现从运算符变成数字的时候，lst分别增加每一个运算符。
# # 每次增加，再把该项设为空字符。


# def splitter(string):
#     lst = []
#     pre = -1        # 0 means num, 1 means char
#     now = -1
#     num = ''
#     char = ''
#     for ii in string:
#         if ii.isdigit():
#             num += ii
#             now = 0
#         else:
#             char += ii
#             now = 1
#         if now == 1 and pre == 0:
#             lst.append(int(num))
#             num = ''
#         elif now == 0 and pre == 1:
#             lst += list(char)
#             char = ''
#         pre = now
#     if now == 0:
#         lst.append(int(num))
#     else:
#         lst += list(char)
#     return lst

# # 简单运算
# # 先定义一个简单运算器，处理不含括号的运算式，遵循先乘除，后加减，从左到右的原则。
# # 定义两个栈，
# # 首先要处理负数，在简单运算中，只有第一个数字可能是负数（标准的表达式）。 所以，如果第一个运算符是取负运算符，先执行之，再入栈。如果不是，直接入栈。
# # 然后执行乘法和除法，因为store栈是正向入栈的，出栈的时候是从表达式的右边向左边，这会出错。所以先把store栈堆入calc栈中。再从calc栈进行从左到右的运算。
# # 每次遇到乘号或者除号就从两个栈各取一个运算，然后入栈store。这样即使是连续乘除也不会错。然后执行加减法，逻辑和乘除一样。


# def simple_calculator(lst):
#     stack_store = Stack()
#     stack_calc = Stack()

#     # Negative
#     if lst[0] == '-':
#         stack_store.push(-lst[1])
#         for ii in lst[2:]:
#             stack_store.push(ii)
#     else:
#         for ii in lst:
#             stack_store.push(ii)

#     # Multiply & Divide
#     while stack_store.size() > 0:
#         stack_calc.push(stack_store.pop())  # 先把栈堆入calc栈当中
#     while stack_calc.size() > 0:
#         element = stack_calc.pop()
#         if element == '*':
#             res = stack_store.pop() * stack_calc.pop()  # 遇到乘号和除号就运算，然后放入store当中
#             stack_store.push(res)
#         elif element == '/':
#             res = stack_store.pop() / stack_calc.pop()
#             stack_store.push(res)
#         else:
#             stack_store.push(element)

#     # addition & subtraction
#     while stack_store.size() > 0:
#         stack_calc.push(stack_store.pop())  # 加减也是同理的
#     while stack_calc.size() > 0:
#         element = stack_calc.pop()
#         if element == '+':
#             res = stack_store.pop() + stack_calc.pop()
#             stack_store.push(res)
#         elif element == '-':
#             res = stack_store.pop() - stack_calc.pop()
#             stack_store.push(res)
#         else:
#             stack_store.push(element)

#     return stack_store.peek()  # 此时store栈中应该只有一个元素，那就是结果了。

# # 计算器（带括号）
# # 处理完了不带括号的，再处理带括号的。
# # 同样的，使用栈进行括号处理。
# # 在前面，我们首先已经获得了一个不带括号的简单运算器，返回值是一个数字（注意，可以是浮点数。但是输入值必须是整型，其实稍微改一改splitter也可以处理浮点运算）
# # 同样的，生成两个栈。从store栈往calc栈移动，如果遇到了左括号，则从calc栈开始出栈元素，放入空列表lst2中。当遇到右括号时，停止出栈，把lst2放入简单计算器中计算结果。
# # 随后，把结果入栈calc。
# # 因为是遇到第一个左括号就开始从calc出栈，直到遇到右括号为止，这样保证了是从最里面的括号开始计算。
# # 运算完之后，又继续出入栈，直到整个队列不含括号。并且全部入栈calc。
# # 随后，calc出栈，再进行一次简单运算，就可以得到结果。


# def calculator(lst):
#     stack_store = Stack()
#     stack_calc = Stack()
#     for ii in lst:
#         stack_store.push(ii)  # 先把列表放入栈中。
#     while stack_store.size() > 0:
#         element = stack_store.pop()  # 从store栈移动向calc栈，遇到左括号执行行为。
#         if element == '(':
#             lst2 = []
#             ele2 = stack_calc.pop()  # 遇到左括号后，从cal栈出栈一个list。这里是不含括号的，执行简单运算。
#             while ele2 != ')':
#                 lst2.append(ele2)
#                 ele2 = stack_calc.pop()
#             # 把简单运算的结果放入calc栈中，同时两个括号正好已经被取出，无视之。
#             stack_calc.push(simple_calculator(lst2))
#         else:
#             stack_calc.push(element)  # 没遇到左括号就直接放入calc
#     lst3 = []
#     for ii in range(stack_calc.size()):  # 最后，剩下一个不含括号的表达式，再次执行。得到最终结果
#         lst3.append(stack_calc.pop())
#     return simple_calculator(lst3)


# # 主程序：
# while True:
#     try:
#         lst = splitter(input())
#         print(calculator(lst))
#     except:
#         break

# # 总结
# # 用堆栈是比较好处理一些需要在字符串中来回的问题的。比如说括号，需要找到最里面的一个，再反向找另一个，用两个堆栈比较合适。
# # 对于从左到右的运算，其实是队列，当然，两个字符串也就是队列了。
# # 对于python来说，用list加上指针，利用切片的办法，完全可以做出一样的行为。
# # 不管是从左到右，还是回头计算。只不过这道题要求了栈，才特地构建了这个类。
# # 当然，人生苦短，如果是面试，我们需要认真的讲解自己的想法。如果是机考，建议直接eval！！

# eval解法：
while True:
    try:
        str_input = input()

        print(eval(str_input))

    except:
        break
