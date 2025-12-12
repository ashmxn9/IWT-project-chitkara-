n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(8):
    for j in range(8):
        if(i+j)%2==0:
            print("#",end="")
        else:
            print(" ",end="")
    print()
for i in range(1,5):
    for j in range(4):
        print(i,end="")
    print()
i=0
while i<3:
    print("hi")
    i+=1
#for i in range(2,10,2):
 #   print(i,end=" ")

for i in range(3):
    for j in range(3):
        print(i,j,end="+")
print()    
n=int(input("enter a number:"))

if n>0:
    print("positive")
elif n<0:
    print("negative")
else:
    print("zero")
    