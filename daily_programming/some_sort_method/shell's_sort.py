'''
希尔排序：小块的插入排序！
'''

def shell_sort(aList):
    n = len(aList)
    step = n // 2 # 增量
    while step > 0:
        for i in range(step, n): # 各子部分插入排序
            while i >= step and aList[i] < aList[i-step]:
                aList[i], aList[i-step] = aList[i-step], aList[i]
                i -= step
        print('排序中间过程：', aList)
        step = step //2

if __name__ == '__main__':
    # li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    li = [49, 38, 65, 97, 76, 13, 27, 48, 55, 4]
    print(li)
    shell_sort(li)
    print(li)