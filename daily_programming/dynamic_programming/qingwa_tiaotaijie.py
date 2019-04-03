'''
一只青蛙一次可以跳上 1 级台阶，也可以跳上2 级。求该青蛙跳上一个n 级的台阶总共有多少种跳法。
答题思路:
如果只有1级台阶，那显然只有一种跳法
如果有2级台阶，那么就有2种跳法，一种是分2次跳。每次跳1级，另一种就是一次跳2级
如果台阶级数大于2，设为n的话，这时我们把n级台阶时的跳法看成n的函数，记为f(n),第一次跳的时候有2种不同的选择：
    一是第一次跳一级，此时跳法的数目等于后面剩下的n-1级台阶的跳法数目，即为f(n-1),
    二是第一次跳二级，此时跳法的数目等于后面剩下的n-2级台阶的跳法数目，即为f(n-2),因此n级台阶的不同跳法的总数为，不难看出就是斐波那契数列!
'''
def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(2))

# 要创建动态规划类
class Dp(object):
    def __init__(self, n):
        self.mark = [0] * (n+1) # 备忘录（动态规划专有名词），记录计算过的结构，初始化为0，长度为台阶数
        print(self.dp(n))
    def dp(self, n):
        self.count = 0 # 当前n个台阶有count种跳法
        if self.mark[n] != 0: # 首先判断是否在备忘录中
            self.count = self.mark[n]
        elif n <= 1: # 然后判断最基础的情况
            self.count = 1 # return 1也可以
        elif n > 1: # 最后子问题重叠
            self.count = self.dp(n-2) + self.dp(n-1)
        self.mark[n] = self.count
        return self.count

Dp(100)