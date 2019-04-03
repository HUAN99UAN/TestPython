'''
背包问题：给定n种物品和一个背包。物品i的重量是Wi，其价值为Vi，背包的容量为C。应如何选择装入背包的物品，使得装入背包中的物品的总价值最大？
假设具体问题数值：A物品，重量为6kg，价值为8元，
         B物品，重量为8kg，价值为13元，
         C物品，重量为10kg，价值为15元
背包可以装为50kg的物品。（选择优先B，然后C，然后A——根据单价）
'''
beg = 50
value = 0
choice = []
while beg > 0:
    if beg > 8:
        beg -= 8
        value += 13
        choice.append('B')
    elif beg > 10:
        beg -= 10
        value += 15
        choice.append('C')
    elif beg > 6:
        beg -= 6
        value += 8
        choice.append('A')
    else:
        break

    print("剩余的背包重量：",beg)
    print("获得的总价值：",value)
    print("选择的物品的类型及顺序：",choice)