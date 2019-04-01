'''
基数排序:
'''
def radix_sort(aList):
    i = 0
    n = 1
    max_num = max(aList)
    while max_num > 10 ** n: # 得到最大数的位数
        n += 1
    while i < n:
        bucket = {}
        for x in range(10): # 将桶置空
            bucket.setdefault(x, [])
        for x in aList:
            radix = int((x/(10**i))%10) # 注意转化为int型，不然报错！
            bucket[radix].append(x)
        j = 0
        for k in range(10):
            if len(bucket[k]) != 0:
                for y in bucket[k]:
                    aList[j] = y
                    j += 1
        i += 1

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    radix_sort(li)
    print(li)