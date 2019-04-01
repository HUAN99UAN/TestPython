'''
插入排序：每次新加一个元素，交换找到合适的位置
'''

# 写法一：
# def insert_sort(aList):
#     n = len(aList)
#     for i in range(0, n):
#         j = i
#         while j > 0:
#             if aList[j] > aList[j-1]:
#                 aList[j], aList[j-1] = aList[j-1], aList[j]
#             j -= 1
# 写法二：
def insert_sort(aList):
    n = len(aList)
    for i in range(0, n):
        while i > 0 and aList[i] > aList[i-1]:
            aList[i], aList[i-1] = aList[i-1], aList[i]
            i -= 1

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    insert_sort(li)
    print(li)