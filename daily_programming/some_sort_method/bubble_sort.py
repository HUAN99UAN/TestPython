'''
冒泡排序：一次冒出一个泡
'''

def bubble_sort(aList):
    n = len(aList)
    for i in range(0, n-1): # n-1趟冒泡
        for j in range(0, n-i-1): # 每次冒出一个，当前趟要比较的次数
            if aList[j] < aList[j+1]:
                aList[j], aList[j+1] = aList[j+1], aList[j]

#  改进：设立tag标记一趟冒泡是否有交换，没有说明已经有序！
def bubble_sort2(aList):
    # tag = 0
    n = len(aList)
    for i in range(0, n-1):
        tag = 0
        for j in range(0, n-i-1):
            if aList[j] < aList[j+1]:
                aList[j], aList[j+1] = aList[j+1], aList[j]
                tag = 1
        if tag == 0:
            break

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # li = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(li)
    bubble_sort(li)
    print(li)

    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    bubble_sort2(li)
    print(li)