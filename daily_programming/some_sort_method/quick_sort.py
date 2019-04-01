'''
快速排序
'''
def partition(aList, left, right):
    key = aList[left]
    low = left
    high = right
    while low < high:
        while (low < high) and (aList[high] > key): # 从右向左扫描比基准小的值；注意(low < high)
            high -= 1
        aList[low] = aList[high]
        while (low < high) and (aList[low] < key): # 从左向右扫描比基准大的值
            low += 1
        aList[high] = aList[low]

        aList[low] = key # 最后把基准放入合适的位置！
    return low

def quick_sort(aList, left, right):
    if left < right:
        mid = partition(aList, left, right)
        quick_sort(aList, left, mid-1)
        quick_sort(aList, mid+1, right)
    return aList

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    n = len(li)
    quick_sort(li, 0, n-1)
    print(li)