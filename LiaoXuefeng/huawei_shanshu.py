# 约瑟夫环问题：（隔2个删除一个，则K = 3，第一个删除的是K- 1 = 2；如下被删除的被标记为 # ）
#  0     1 2 3 ... K-2  # K  K+1 K+2 ... n-1
# n-K'             n-2'   0'  1'  2' ... n-K-1'
# 删除一个后，新的编号相对于之前偏移了K
# 如果最后剩下1个人，则一定是删除第0个。得到f[1]=0。最后得到递推公式：
# f[1] = 0
# f[n] = (f[n - 1] + K) mod n
while True:
    try:
        n = int(input())
        def last(n, k):
            # 最后一轮，只有一个元素
            last = 0
            # 前面n - 1轮
            for i in range(2, n+1):
                last = (last + k) % i
                print(last)
            return last
        print(last(n, 3))
    except:
        break

# 法二:数组0-count，然后每次隔2次（n用来计数）
while True:
    try:
        count = int(input())
        l = list(range(0, count))
        n = 0
        while len(l) > 1:
            for i in l[:]: # 必须是l[:], 不能是l
                if n == 0 or n == 1:
                    n += 1
                    continue
                else:
                    l.remove(i)
                    n = 0
        print(l[0])
    except:
        break