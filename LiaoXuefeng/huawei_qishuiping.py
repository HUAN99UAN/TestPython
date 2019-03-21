def qishuiping(n):
    c = 0
    if n < 2:
        return 0
    while n > 2:
        c += n//3
        n = n//3 + n%3
    if n == 2:
        c += 1
    return c

data= []
while True:
    try:
        data.append(int(input()))
    except:
        result = []
        for i in data:
            if i != 0:
                result.append(qishuiping(i))
        for i in result:
            print(i)
        break

