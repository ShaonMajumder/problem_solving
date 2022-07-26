class Node:
    def __init__(self,datavalue=None):
        self.datavalue = datavalue
        self.nextvalue = None

n1 = Node('A')
n1.nextvalue = Node('B')
n1.nextvalue.nextvalue = Node('C')

def printLinkedList(n1):
    current_element = n1
    temp = []
    while current_element:
        temp.append(current_element.datavalue)
        current_element = current_element.nextvalue
    return temp

print(printLinkedList(n1))
