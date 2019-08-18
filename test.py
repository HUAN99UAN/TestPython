while True:
    try:
        n = int(input())
        l = list(map(int, input().split(' ')))

        min = abs(l[0] - l[1])
        min_index = 0
        for i in range(1, n - 1):
            if abs(l[i] - l[i + 1]) < min:
                min = abs(l[i] - l[i + 1])
                min_index = i
        print(l[min_index], l[min_index + 1])
    except:
        break

while True:
    try:
        n = int(input())
        l = list(map(int, input().split(' ')))

        cnt = 0
        for i in range(0, n-1):
            for j in range(i+1, n):
                max_one = max(l[i], l[j])
                min_one = min(l[i], l[j])
                if min_one >= max_one * 0.9:
                    cnt += 1
        print(cnt)
    except:
        break