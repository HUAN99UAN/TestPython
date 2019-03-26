while True:
    try:
        data = input()
        a = data.split() # 以空白符分割字符串
        print(int(a[0]) + int(a[1]))
    except:
        break

# 另一种接收多行输入——实现多次a+b
# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))

# N, M = map(int, input().split()) # map将字符串转化为int，如果输出N, M，则是（N, M）元组的形式！
# grades = list(map(int, input().split())) # list将映射的结果转化为列表！
# start, end = sorted([int(a[0]), int(a[1])]) # sorted排序的内容是可迭代对象——列表[]，字典等。

# import collections
# record = collections.OrderedDict() #  这个类型在添加键的时候会保持顺序,因此键的迭代总是一致的

# sorted()与list.sort()的不同
# 　　1）list.sort() 方法返回none，sorted()返回结果
# 　　2）list.sort() 方法只可以供列表使用，而 sorted() 函数可以接受任意可迭代对象（iterable）

# for i in t:
#     if (i not in result):
#         result.append(i)
# # 可以等价于set()函数去重
# t = set(t)
# for i in t:
#     result.append(i)

# print(int(input(),16)) # int() 函数用于将一个字符串或数字转换为整型。