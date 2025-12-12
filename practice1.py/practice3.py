n=int(input("enter the no: "))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)
#18
n=int(input("enter the no :"))
for i in range(1,11):
    print(n,'*',i,'=',n*i)
for i in range(5):
    for j in range(5):
        print("*",end="")
    print()
numbers=[5,6,7,3,5,5]
count_5=numbers.count(5)
print("number of times 5 appears:",count_5)
students={'A':85,'B':92,'C':78,'D':95,'E':88}
top=max(students,key=students.get)
print('topper:',top,students[top])
#
n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
        print()