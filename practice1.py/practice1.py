t=(100,200,300,400)
#indexing
print(t[0]) #output:100
#slicing
print(t[1:3]) #output:(200,300)
#length
print(len(t)) #output:4
#membership check
print(200 in t) #output:True
#count and index
print(t.count(300)) #output:1
print(t.index(400)) #output:3
a=10
b=20
a,b=b,a
print(a,b)
#upper lower
text="hello world"
print(text.upper()) #output:HELLO WORLD
text="PYTHON IS FUN"
print(text.lower()) #output:python is fun
text="my name is ashmanpreet singh"
print(text.title()) #output:My Name Is Ashmanpreet Singh
text="my name is ASHMANPREET"
print(text.capitalize()) #output:My name is ashmanpreet
text="Hello Ashmanpreet"
print(text.swapcase()) #output:hELLO aSHMANPREET
text="  ashmanpreet singh  "
print("before strip:",text)
print("after strip:",text.strip())
#lstrip()=removes spaces from the left side
#rstrip()=removes spaces from the right side
text="my name is ashmanpreet singh"
print(text.replace("ashmanpreet","john")) #output:my name is john singh
text="my name is ashmanpreet singh"
words=text.split()
print(words)
text="ashman"
print(text.center(20,"*")) #output:*******ashman********
print(text.ljust(20,"-")) #output:ashman--------------
print(text.rjust(20,"+")) #output:+++++++++++++++ashman
text="Hello\nWorld\nPython"
lines=text.splitlines()
print(lines)
text="hello\tworld"
print(text.expandtabs(4)) #tab becomes 4 spaces
#lists
my_list=[10,20,30,40,50]
print(my_list)
fruits=["apple","banana","mango","orange"]
print(fruits[0]) #output:apple
print(fruits[2]) #output:mango
print(fruits[-1]) #output:orange  
fruits[1]="grape"
print(fruits) #output:['apple', 'grape', 'mango', 'orange']
numbers=[1,2,3]
numbers.append(4) #add 4 at the end
numbers.insert(1,5) #insert 5 at index 1
numbers.extend([6,7]) #add multiple elements
print(numbers)
numbers.remove(3) #remove 3
numbers.pop() #remove last item
print(numbers)
#tuples
my_tuple=(10,20,30,40)
print(my_tuple)
fruits=("apple","banana","mango","orange")
print(fruits[0]) #output:apple
print(fruits[2]) #output:mango
print(fruits[-1]) #output:orange
t1=(1,2,3)
t2=(4,5,6)
#concatenation
t3=t1+t2   
print(t3) #output:(1, 2, 3, 4, 5, 6)
#repetition
print(t1*2) #output:(1, 2, 3, 1, 2, 3)
#length
print(len(t2)) #3
#membership 
print(5 in t2) #True
#sets
my_set={10,20,30,40}
print(my_set) #does not allow duplicates, unordered , curly braces
numbers={1,2,3,4,4,5}
print(numbers) #duplicates removed: {1, 2, 3, 4, 5}
#using set() constructor
text_set=set("hello world")
print(text_set)
fruits={"apple","banana"}
fruits.add("mango") #add single element
fruits.update(["orange","grape"]) #add multiple elements
print(fruits)
fruits.remove("banana") #remove element
fruits.discard("kiwi") #does not raise error if element not found
fruits.pop() #removes a random element
print(fruits)
a={1,2,3}
b={3,4,5}
print(a|b)
print(a&b) #{3}
print(a-b) #{1, 2}
print(a^b) #{1, 2, 4, 5}
#dictionaries
student={
"name":"ashman",
"age":18,
"marks":92
}
print(student)
print(student["name"]) #output:ashman
print(student["marks"]) #output:92
student["city"]="amritsar"
print(student) #output: {'name': 'ashman', 'age': 18, 'marks': 92, 'city': 'amritsar'}
student["marks"]=95 #update marks
print(student) #output: {'name': 'ashman', 'age': 18, 'marks': 95, 'city': 'amritsar'}
student.pop("age") #remove age
print(student) #output: {'name': 'ashman', 'marks': 95, 'city': 'amritsar'}
del student["marks"]
print(student) #output: {'name': 'ashman', 'city': 'amritsar'}
if"name" in student:
    print("yes,name exists") #output:yes,name exists
#merging dictionaries
d1={"a":1,"b":2}
d2={"c":3,"d":4}
d1.update(d2)
print(d1) #output: {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
#loops
for i in range(1,6):
    print(i)
for i in range(1,10,2):
    print(i)
fruits=["apple","banana","mango"]
for f in fruits:
    print(f)
i=1
while i<=5:
    print(i)
    i+=1
i=2
while i<=10:
    print(i)
    i+=2
for i in range(1,6):
    if i==3:
        break
    print(i)
for i in range(1,4):
    for j in range(1,4):
        print(i,j)
for i in range(1,5):
    print(i)
else:
    print("loop completed")
for i in range(1,5):
    if i==3:
        break
    print(i)
else:
    print("will not print")
name="ashman"
for ch in name:
    print(ch)
student={"name":"ashman","age":18,"marks":92}
for key, value in student.items():
    print(key,"=>",value)
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix:
    for val in row:
        print(val,end=" ")
    print()
while True:
    print("hello")
    break
text="ashman"
vowels=0
for ch in text:
    if ch in "aeiou":
        vowels+=1
print("vowels:",vowels)
