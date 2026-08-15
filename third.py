#operator precedence
#(),list x[i],slicing s[1:2],power,~bitwise not,*,/,//,% (left to write);<<,>>;bitwise &,^bitwise ,|bitwise,(in,not,in,is,is not),not,and ,or,if else,lambda,==assignment
#function definition 
def hello():
    print("Hello!! how are you")
print("top")
hello()
print("bottom")
#defining a function with parameters
def fun(user):
    print("welcome "+user)
fun("gysana")
#function with multiple parameters
def fun1(user,roll):#we can use it here as roll is integer type to create it in string str(roll)
    print("welcome "+user+" your roll no is "+roll)
fun1("gysana","62")
def max(n1,n2,n3):#formal parameters
    if n1>n2 and n1>=n3:
        return n1
    elif n2>=n3 and n2>=n1:
        return n2
    else:
        return n3
result=max(40,20,30)#actual parameters
print(result)
def cube(n1):
    return n1*n1*n1
num=int(input("enternumber "))
result1=cube(num)
print(result1)
def evenorodd(n2):
    if(n2%2==0):
        print("even")
    else:
        print("odd")
evenorodd(3)
def mod(n):
    return n%2==0
b=mod(5)
print(b)
#loops we have entry control loops in python, 1 intiliazation,condition,updation;no post pre increments in python
i=1
while(i<=10):#while loop
    print(i)
    i+=1
print("outside loop")
#for loop
# for variable(any variable that we have to use loop) in sequence(a collevtion of items like set,dictionary ,touple,string,range of numbers)
for i in range(10):   #it will print 0 to 9 
    print(i)
for i in range(1,10):   #it will print 1 to 9 
    print(i)
for i in range(1,10,2):   #it will print 0 to 9(start,stop-1,step prints even )
    print(i)
for i in "gysana":
    print(i)
l=[1,34,2,3]
for i in l:
    print(l)
    print(l[2])