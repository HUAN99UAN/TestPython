'''
归并排序
'''
def merge(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i == len(a): # 说明a数组么有元素了！
        for x in b[j:]:
            c.append(x)
    else:
        for x in a[i:]:
            c.append(x)
    return c

def merge_sort(aList):
    n = len(aList)
    if n <= 1:
        return aList
    mid = n//2
    left = merge_sort(aList[:mid])
    right = merge_sort(aList[mid:])
    return merge(left, right)

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    print(merge_sort(li))