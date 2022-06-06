# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
dict = OrderedDict()
N = int(input())
for i in range(N):
    line_inputs = input().split()
    v = int(line_inputs[-1])
    k = " ".join(line_inputs[:-1])
    if k in dict:
        dict[k] = dict[k] + float(v)
    else:
        dict[k] = float(v)


for i in dict:
    print(i,int(dict[i]))