
# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin
team=[]
while True:
    line = stdin.readline().strip()
    if line=='':
        break
    item = line.split(' ')
    item = [int(i) for i in item]
    team.append(item)

print(item)