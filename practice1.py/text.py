#9
text="python programming is easy"
print(text.title())
#10
text=" hello python "
print(text.strip())
#11
text="amazing"
print(text.replace("a","@"))
#12
text="welcome to python"
print(text.capitalize())
#sectionD
#13
a=2
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
#14
num=int(input("enter a number"))
if num%2==0:
    print("even")
else:
    print("odd")
#16
for i in range(1,50):
    if i%2==0:
        print(i)
#17
n=int(input())
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)
#15
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)


