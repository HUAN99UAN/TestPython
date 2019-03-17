'''
    设N是一个四位数，它的9倍恰好是其反序数（例如：1234 的反序数是4321），求N的值。
'''
def number(n):
    c = 0
    while (n > 0):
        a = n % 10
        n = n // 10
        c = c * 10 + a
    return c

for i in range(1000, 10000):
    n = number(i)
    if i * 9 == n:
        print(i)