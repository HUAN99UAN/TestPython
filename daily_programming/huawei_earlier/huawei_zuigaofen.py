while True:
    try:
        N, M = map(int, input().split()) # map将字符串转化为int，如果输出N, M，则是（N, M）元组的形式！
        grades = list(map(int, input().split())) # list将映射的结果转化为列表！
        for i in range(M):
            act = input().split()
            if act[0] == 'Q':
                start, end = sorted([int(act[1]), int(act[2])]) # sorted排序的内容用列表[]
                print(max(grades[start-1 : end]))
            else:
                grades[int(act[1])-1] = int(act[2])
    except:
        break