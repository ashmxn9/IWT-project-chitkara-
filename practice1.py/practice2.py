for i in range(10,0,-1):
    print(i)
for i in range(3,31,3):
    print(i)
for i in range(5):
    pass #do nothing
for i in range(1,6):
    print("*"*i)
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
rows=5
for i in range(rows):
    print(" "*(rows-i-1)+"*"*(2*i+1))
for i in range(1,4):
    for j in range(1,4):
        print(i,j)
for i in range(1,6):
    for j in range(1,6):
        if j%2==0:
            print("*",end=" ")
        else:
            print("-",end=" ")
    print()
    