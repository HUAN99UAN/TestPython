vertex, edge = map(int, input('input the number of vertex and edge:').split())
dis = [[0]*vertex]*vertex # 初始化二维数组
print('input the distance matrix:')
for i in range(vertex):
    dis[i] = input().split()
    dis[i] = [int(j) for j in dis[i]]
print(dis)
