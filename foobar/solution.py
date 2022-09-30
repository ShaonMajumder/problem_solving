def solution(x,y):
    if len(x) == len(y):
        return False

    if len(x) > len(y):
        superset = x
        subset = y
    else:
        superset = y
        subset = x
        
    superset_dic = {}
    
    count = 0
    for i in subset:
        if i in superset_dic:
            superset_dic[i] += 1
        else:
            superset_dic[i] = 1
        if i == superset[count]
        count += 1
    
    for i in superset:
        if i in superset_dic and int(superset_dic[i]) > 0:
            superset_dic[i] -= 1
        else:
            return i

    print(superset_dic )
x = list( input().split() )
y = list( input().split() )
print( solution(x,y) )
# print(superset_dic)