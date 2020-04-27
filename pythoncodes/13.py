row=int(input("enter the number of rows:"))
column=int(input("enter the number of columns:"))
matrix=[]
for i in range(0,row):
    rown=[]
    for j in range(0,column):
        c=int(input(f"enter the element {i}{j}:"))
        rown.append(c)
    matrix.append(rown)
for i in range(0,row):
    for j in range(0,column):

        print(matrix[i][j],end=" ")
    print()
