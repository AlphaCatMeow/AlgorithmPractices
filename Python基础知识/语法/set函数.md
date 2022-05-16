# Python的Set函数

## 描述

  set函数是Python的内置函数，用于创建一个空集合，或者将一个可迭代对象转化为一个无序集合。

## 语法

  ```python
  set(iterable)
  ```

## 参数说明

  | 名称       | 含义                          | 备注                              |
  |:--------:|:---------------------------:|:-------------------------------:|
  | iterable | 待转化为无序集合的可迭代对象，包括列表、字符串和字典等 | 可省略的参数。当该参数省略时，将创建一个不包含任何元素的空集合 |

## 举例

### 1. 无参

  创建一个空集合赋给一个变量，输出变量的类型和值：

  ```python
  a = set() 

  print(type(a))
  print(a)
  ```

   输出结果为：

  ```python
  <class 'set'>
  set()
  ```

  此时变量a是集合类型，没有任何元素。

### 2. 将字符串转化为集合

  ```python
  a = 'I love Python3!'

  b = set(a)

  print(b)
  ```

  输出结果为：

  ```python
  {'v', 't', '!', 'e', 'h', '3', 'l', 'y', 'n', ' ', 'o', 'P', 'I'}
  ```

### 3. 将列表转化为集合

  ```python
  a = []
  b = [23, 45, 6, 7, 21, 22, 530, 'wdf']

  print(set(a))
  print(set(b))
  ```

  输出结果为：

  ```python
  set()
  {6, 7, 45, 530, 21, 22, 23, 'wdf'}
  ```

### 4. 将元组转化为集合

  ```python
  a = ()
  b = (23, 45, 6, 7, 23, 22, 530, 'wdf')

  print(set(a))
  print(set(b))
  ```

  输出结果为：

  ```python
  set()
  {6, 7, 'wdf', 45, 530, 22, 23}
  ```

### 5. 将字典转化为集合

  ```python
  a = {}
  b = {'China':'Beijing', 'Japan':'Tokyo', 'Mongolia':'Ulan Bator'}

  print(set(a))
  print(set(b))
  ```

  输出结果为：

  ```python
  set()
  {'Japan', 'Mongolia', 'China'}
  ```

  可以看出将字典转化为集合时，只是收录了字典中的key。

## 6. 多个重复元素的可迭代对象

  ```python
  a = 'wwwwwwwwww'
  b = [1,1,1,1,1,1]
  c = ('sdf', 'sdf', 'sdf')
  d = {1:12, 2:23, 1:345}

  print(set(a))
  print(set(b))
  print(set(c))
  print(set(d))
  ```

  输出结果：

  ```python
  {'w'}
  {1}
  {'sdf'}
  {1, 2}
  ```

## 注意事项

1. 当使用set的有参函数时，参数必须是可迭代对象。当参数不是可迭代对象时，Python会抛出异常。例如：

    ```python
    a = 1.23

    print(set(a))
    ```

    结果：

    ```python
    Traceback (most recent call last):
      File "Test.py", line 3, in <module>
        print(set(a))
    TypeError: 'float' object is not iterable
    ```

    异常会提示float类型不是可迭代的。

2. 转化为集合后，序列是随机的，可能跟转化前的序列不同。

3. 由于集合不包含重复元素，使用set()函数后会将之前的可迭代序列中的重复元素删除。

4. 将字典转化为集合，仅仅只是将键（key）收录到集合中。如果想将字典中的值转化为集合，可以用字典函数values()
