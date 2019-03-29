'''
选择排序:第一趟，从 n 个记录中找出关键码最小的记录与第 1 个记录交换……
'''

def select_sort(aList):
    n = len(aList)
    for i in range(0, n):
        for j in range(i+1, n):
            if aList[j] > aList[i]:
                aList[j], aList[i] = aList[i], aList[j]

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    select_sort(li)
    print(li)