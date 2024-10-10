row,col=int(input("Row = ")),int(input('Col = '))
matrix = [[int(input()) for _ in range(col)] for _ in range(col)]
#Brute Force Approach
def markRow(a,col,i):
    for j in range(col):
        a[i][j] = -1

def markCol(a,row,j):
    for i in range(row):
        a[i][j] = -1

def brute_force():
    
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                markRow(matrix,col,i)
                markCol(matrix,row,j)
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
            print(matrix[i][j],end=" ")
        print()

#Better Approach
def better_approach():
    r = [0] * row
    c = [0] * col

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                r[i] = 1
                c[j] = 1
    for i in range(row):
        for j in range(col):
            if r[i] or c[j]:
                matrix[i][j] = 0
            print(matrix[i][j],end=" ")
        print()

#Optimal Approach
def optimal_approach():
    col0 = 1
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j !=0:
                    matrix[0][j] = 0
                else:
                    col0=0

    for i in range(1,row):
        for j in range(1,col):
            if matrix[i][j] != 0:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
    if matrix[0][0] == 0:
        for j in range(col):
            matrix[0][j] = 0
    if col0 == 0:
        for i in range(row):
            matrix[i][0] = 0
    printing(matrix)

def printing(a):
    for i in range(row):
        for j in range(col):
            print(matrix[i][j],end=" ")
        print()

optimal_approach()