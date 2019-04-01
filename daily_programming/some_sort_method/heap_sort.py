'''
堆排序
'''
def heap_adjust(aList, low, high):
    i = low # 父节点
    j = 2 * i +1 # 左子节点
    tmp = aList[i] # 父节点值，先存储下来
    while j <= high: # 子节点在节点中
        if j < high and aList[j] < aList[j+1]: # 有右节点且右节点比较大
            j += 1 # 往大根走
        if tmp > aList[j]:
            break
        else:
            aList[i] = aList[j]
            i = j
            j = 2 * i + 1
    aList[i] = tmp # 将替换的父节点值赋给最终的父节点

def heap_sort(aList):
    n = len(aList)
    # 创建堆0—n-1
    for i in range(n//2 -1, -1, -1):
        heap_adjust(aList, i, n-1)

    # 挨个出数
    for i in range(n-1, -1, -1):
        aList[0], aList[i] = aList[i], aList[0]
        heap_adjust(aList, 0, i-1)


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    heap_sort(li)
    print(li)