# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict;
dict = OrderedDict()
N = int(input())
for i in range(N):
    word = input()
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1
        
print(len(dict))
print(" ".join([str(dict[i]) for i in dict]))