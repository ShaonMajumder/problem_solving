from collections import defaultdict

def solution(x, y):
    def helper(subset, superset):
        dic = defaultdict(lambda : 0)

        for i in subset:
            dic[i] += 1

        for i in superset:
            dic[i] -= 1
            if dic[i] < 0:
                return i

    if len(x) > len(y):
        return helper(y,x)
    else:
        return helper(x,y)
    

print( solution( [4,5,6,6,6], [4,5,6,6]) )