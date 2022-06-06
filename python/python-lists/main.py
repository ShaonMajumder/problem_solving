if __name__ == '__main__':
    li = []
    N = int(input())
    for i in range(N):
        inputs = input().split()
        if len(inputs) > 1:
            action = inputs[0]
            operands = list(map(int,inputs[1:]))
            
        else:
            action = inputs[0]
            
        if action == "insert":
            index, integer = operands
            li.insert(int(index),integer)
        elif action == "print":
            print(li)
        elif action == "remove":
            operand = operands[0]
            li.remove(operand)
        elif action == "append":
            operand = operands[0]
            li.append(operand)
        elif action == "sort":
            li.sort()
        elif action == "pop":
            li.pop()
        elif action == "reverse":
            li.reverse()