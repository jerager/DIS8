

example = [
    5,3,4,6,7,8,9,1,2,
    6,7,2,1,9,5,3,4,8,
    1,9,8,3,4,5,5,6,7,
    8,5,9,7,6,1,4,2,3,
    4,2,6,8,5,3,7,9,1,
    7,1,3,9,2,4,8,5,6,
    9,6,1,5,3,7,2,8,4,
    2,8,7,4,1,9,6,3,5,
    3,4,5,2,8,6,1,7,9]

exampleRight = [
    5,3,4,6,7,8,9,1,2,
    6,7,2,1,9,5,3,4,8,
    1,9,8,3,4,2,5,6,7,
    8,5,9,7,6,1,4,2,3,
    4,2,6,8,5,3,7,9,1,
    7,1,3,9,2,4,8,5,6,
    9,6,1,5,3,7,2,8,4,
    2,8,7,4,1,9,6,3,5,
    3,4,5,2,8,6,1,7,9]

class JPrint():
    def __str__(self):
        return self.type+str(self.stored)


class Row(JPrint):
    def __init__(self,i=0):
        self.stored = [i]
        self.type = "Row"
        
class Column():
    def __init__(self,i):
        self.stored = [i]
        self.type = "Column"
        
def groups(board):
    yield Row()
    i=1
    while i<9:
        yield Row(i)
        i=i+1
    while i<18:
        yield Column(i)
        i=i+1
    while i<27:
        yield [i]
        i=i+1
        
def printThem(board):
    checks = groups(board)
    for group in checks:
        print(group)

def groupThem(board):
    checks = groups(board)
    list = []
    for group in checks:
        list.append(group)
    return list
    

def printBoard(b):
    print(b[0:9])
    print(b[9:18])
    print(b[18:27])
    print(b[27:36])
    print(b[36:45])
    print(b[45:54])
    print(b[54:63])
    print(b[63:72])
    print(b[-9:])

printBoard(example)

print("Calling printThem")
printThem(example)

all = groupThem(example)

print("Printing groups")
print(all)

