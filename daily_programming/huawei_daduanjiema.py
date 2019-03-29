while True:
    try:
        num = int(input())
        data = input()
        lst = [0] * num  # 不用append就用这个
        for i in range(num):
            start = i * 9
            end = (i + 1) * 9
            lst[i] = data[start:end]

        for i in range(num):
            if lst[i][0] == '0':
                lst[i] = lst[i][::-1]
                lst[i] = lst[i][0:8]
            else:
                lst[i] = lst[i][1:9]

        print(' '.join(str(i) for i in lst))
    except:
        break