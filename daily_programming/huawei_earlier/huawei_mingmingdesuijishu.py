import random

# # 随机产生的数组元素去重，排序
# def suijishu(n):
#     t = []
#     result = []
#     while n >= 1:
#         t.append(random.randint(1, 1000)) # 随机整数；random.uniform(a, b)随机浮点数
#         n -= 1
#     for i in t:
#         if (i not in result):
#             result.append(i)
#
#     result = sorted(result)
#     return result
#
# print(suijishu(input()))
while True: # 重点！！！
    try: # 重点！！！
        n = int(input())
        if n <= 0:
            exit()
        t = []
        result = []
        while n >= 1:
            t.append(int(input())) # 根据测试用例
            n -= 1
        for i in t:                # set()函数可以去重，见下方
            if (i not in result):
                result.append(i)

        # result = sorted(result)
        result.sort()
        for i in result:
            print(i)
    except: # 重点！！！
        break # 重点！！！