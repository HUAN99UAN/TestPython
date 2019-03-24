# 华为【数独】
import sys

def isOk(mat, i, j, num):  # 判断填入数字是否合法
    for row in range(0, 9):  # 遍历该列，若该数字已出现过，则不合法
        if mat[row][j] == num:
            return False
    for col in range(0, 9):  # 遍历该行，若该数字已出现过，则不合法
        if mat[i][col] == num:
            return False
    ii = i // 3
    jj = j // 3
    for row in range(ii * 3, ii * 3 + 3):  # 遍历该位置所处的3*3矩阵，若该数字已出现过，则不合法
        for col in range(jj * 3, jj * 3 + 3):
            if mat[row][col] == num:
                return False
    return True


def dfs(mat, i, j):  # 深度优先遍历
    if i == 9:  # 所有行已遍历完，则结束
        return mat
    if j == 9:  # 所有列已遍历完，则进入到下一行
        return dfs(mat, i + 1, 0)
    flag = False  # flag表示该行有需要填充的格子
    for col in range(j, 9):  # 遍历该行的所有列，如果有值为0，则需要进行填充;(0,9)也可以，只是没有必要！前面已经检查过！
        if mat[i][col] == 0:
            flag = True
            isChange = False  # ischange表示是否已进行填充
            for num in range(1, 10):
                if isOk(mat, i, col, num):  # 找出1-9中能够合法填入的数字
                    isChange = True
                    mat[i][col] = num
                    tpp = dfs(mat, i, col + 1)  # 将该位置填充后，该行的后续位置是否有解
                    if tpp == None:  # 如果后续位置无解，则将该位置重新置为0，未填充状态——回溯
                        isChange = False
                        mat[i][col] = 0
                        continue  # 尝试下一个数字
                    else:
                        return tpp
            if isChange == False:  # 找不到合法数字进行填充
                return None
    if flag == False:  # 该行所有位置已填满，进入到下一行
        return dfs(mat, i + 1, 0)


while True:
    isCon = True
    mat = []
    for i in range(9):
        line = sys.stdin.readline().strip() # input()方法和stdin()类似，实现标准输入，不同的是input()括号内可以直接填写说明文字
        if not line:
            isCon = False
            break
        line = [int(i) for i in line.split(' ')] # split默认分割：所有的空字符，包括空格、换行(\n)、制表符(\t)等
        mat.append(line)
    if isCon == False:
        break
    mat = dfs(mat, 0, 0)
    for line in mat:
        print(' '.join(str(j) for j in line))

# //在取得结果后，添上如下代码就可避免83.33%了——牛客网是不完全通过，本地IDE显示正确
# if(data[6][0]==2&&data[6][1]==1&&data[6][2]==3)
# {
#     data[6][2]=5;data[6][3]=8;data[6][4]=4;data[6][5]=6;data[6][6]=9;data[6][7]=7;data[6][8]=3;
#     data[7][0]=9;data[7][1]=6;data[7][2]=3;data[7][3]=7;data[7][4]=2;data[7][5]=1;data[7][6]=5;data[7][7]=4;data[7][8]=8;
#     data[8][0]=8;data[8][1]=7;data[8][2]=4;data[8][3]=3;data[8][4]=5;data[8][5]=9;data[8][6]=1;data[8][7]=2;data[8][8]=6;
# }

# message = sys.stdin.readlines() # readlines区别于readline
# abc
# <CTRL-D>
#
# # message == ['abc\n']