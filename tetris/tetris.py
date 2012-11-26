import random
Field=[[".",".",".",".",".",".","."],
           [".",".",".",".",".",".","."],
           [".","X",".",".",".",".","."],
           ["X","X",".",".",".",".","."],
           ["X","X","X","X","X","X","X"],]
#Pieces=["XX\nXX"]
Pieces=[
"""XX
XX""",
"""XX
 XX""",
""" XX
XX""",
"""XXXX""",
"""X
X
XXX""",
"""  X
XXX""",
""" X
XXX"""]
def draw():
    for row in Field:
        for cell in row:
            print(cell,end="")
        print("")

def DropOneLine(row):
    for i in range(row,0,-1):
        temp=Field[i]
        Field[i]=Field[i-1]
        Field[i-1]=temp

def ClearLine(row):
    for i in range(0, len(Field[row])):
        Field[row][i]="."
    DropOneLine(row)
    CheckLines()

def CheckLines():
    for i in range(len(Field) - 1,0,-1):
        RowClear=True
        for cell in Field[i]:
            if(cell!="X"):
                RowClear=False
        if (RowClear==True):
            ClearLine(i)
            return

def Game():
    while True:
        draw()
        print("\n")
        CheckLines()
        input()

#Game()
print (random.choice(Pieces))
