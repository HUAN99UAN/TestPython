from sys import stdin

n = int(input())
data = []
result = []
while True:
    line = stdin.readline().strip()
    if line == '':
        break
    a = line.split(',')
    data.append(a)

row = len(data)
while len(data[0]):
    for k in range(row):
        for i in range(n):
            if len(data[k]):
                result.append(data[k][0])
                del data[k][0]
            else:
                break
    row = len(data)

print(','.join(result), end='')

# 通过40%