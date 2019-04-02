flag = int(input('please input type of graph(1:directed '
             'graph; 2:undirected graph): '))
vertex, edge = map(int, input('please input the number of vertex and edge: ').split())

dis = []
path = []
inf = 9999
# 初始化邻接矩阵和路径矩阵
for i in range(vertex):
    dis += [[]]
    for j in range(vertex):
        if i == j :
            dis[i].append(0)
        else:
            dis[i].append(inf)
# print(dis) # [[0, 9999, 9999, 9999], [9999, 0, 9999, 9999], [9999, 9999, 0, 9999], [9999, 9999, 9999, 0]]假设输入4 5
for i in range(vertex):
    path += [[]]
    for j in range(vertex):
        path[i].append(-1)
# print(path) # [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]

# 获取输入的值作为邻接矩阵的具体数值并输出邻接矩阵
print('please input weight info(v1 v2 w[v1,v2]): ')
for i in range(edge):
    u, v, w = map(int, input().split())
    if flag == 1:
        dis[u][v] = w
    elif flag ==2:
        dis[u][v] = w
        dis[v][u] = w
print('the weight matrix is:')
for i in range(vertex):
    for j in range(vertex):
        if dis[i][j] != inf:
            print('%5d' % dis[i][j], end='')
        else:
            print('%5s' % '∞', end='')
    print()

# Floyd算法
for k in range(vertex):
    for i in range(vertex):
        for j in range(vertex):
            if dis[k][j]+dis[i][k] < dis[i][j]:
                dis[i][j] = dis[k][j]+dis[i][k]
                path[i][j] = k
print(dis)
print(path)

# 获取路径并输出
def get_path(i, j):
    while i != -1:
        print(i, '- ', end='')
        i = path[i][j]
    print(j)

get_path(1, 0)

# 测试数据：https://www.cnblogs.com/Ash-ly/p/5920953.html?tdsourcetag=s_pcqq_aiomsg
# 2
# 5 7
#
# 0 1 3
# 0 2 5
# 1 2 10
# 1 3 4
# 1 4 1
# 2 3 5
# 3 4 1

# 法二：
# import numpy as np
#
# INFINITY = 65535                        #代表无穷大
# D = np.array([[0,10,INFINITY,INFINITY,INFINITY,11,INFINITY,INFINITY,INFINITY],#邻接矩阵，np.array创建数组
#         [10,0,18,INFINITY,INFINITY,INFINITY,16,INFINITY,12],
#         [INFINITY,18,0,22,INFINITY,INFINITY,INFINITY,INFINITY,8],
#         [INFINITY,INFINITY,22,0,20,INFINITY,INFINITY,16,21],
#         [INFINITY,INFINITY,INFINITY,20,0,26,INFINITY,7,INFINITY],
#         [11,INFINITY,INFINITY,INFINITY,26,0,17,INFINITY,INFINITY],
#         [INFINITY,16,INFINITY,24,INFINITY,17,0,19,INFINITY],
#         [INFINITY,INFINITY,INFINITY,16,7,INFINITY,19,0,INFINITY],
#         [INFINITY,12,8,21,INFINITY,INFINITY,INFINITY,INFINITY,0]])
# lengthD = len(D)                    #邻接矩阵大小
# p = list(range(lengthD))
# P = []
# for i in range(lengthD):
#     P.append(p)
# P = np.array(P)
#
# for i in range(lengthD):
#     for j in range(lengthD):
#         for k in range(lengthD):
#             if(D[i,j] > D[i,k]+D[j,k]):         #两个顶点直接较小的间接路径替换较大的直接路径
#                 P[i,j] = P[j,k]                 #记录新路径的前驱
# print(P)
# print(D)