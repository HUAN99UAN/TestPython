def prime(n):
    if n <= 2:
        return 0
    is_right = [True] * n
    is_right[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_right[i]:
            for j in range(i * i, n, i):
                is_right[j] = False
    m = 0
    for x in range(2, n):
        if is_right[x]:
            m += 1
    return m
print("素数总数：", prime(8))
