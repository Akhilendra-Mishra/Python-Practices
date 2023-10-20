#1
#1 3
#1 3 5
#1 3 5 7
#1 3 5 7 9

row = int(input("enter the no of rows:"))
for i in range(row):
    for j in range(i+1):
        print(j*2-1, end=' ')
    print()
