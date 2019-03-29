'''
冒泡排序：一次冒出一个泡
'''

def bubble_sort(aList):
    n = len(aList)
    for i in range(0, n-1): # n-1趟冒泡
        for j in range(0, n-i-1): # 每次冒出一个，当前趟要比较的次数
            if aList[j] < aList[j+1]:
                aList[j], aList[j+1] = aList[j+1], aList[j]

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    bubble_sort(li)
    print(li)