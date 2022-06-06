from itertools import *
# Enter your code here. Read input from STDIN. Print output to STDOUT
K,M = map( int, input().split())
Lis = []
sum = 0
for i in range(K):
    inputs = list( map( int, input().split()) )
    Ni = inputs[0]
    Li = inputs[1:]
    Lis.append(Li)
    sum += max(Li)**2
for i in product(*Lis):
    print(i)
# print(sum % M)