  #lab 1 (p1)
num1=int(input("enter first number "))
num2=int(input("enter second number"))
choice =input("enter operation (+,*,-,/)")
if choice=="+":
    print("Answer = ",num1+num2)
elif choice=="-":
    print("Answer = ",num1-num2)
elif choice=="*":
    print("Answer = ",num1*num2)
elif  choice=="/":
    print("Answer = ",num1/num2)
else:
     print("invalid operation")
     #p2
score=float(input("enter your score"))
if score>90 and score<=100:
    print("grade A")
elif score>=80:
    print("grade B")
elif score>=70:
    print("grade C")
elif score>=60:
    print("grade D")
elif score>=50:
    print("grade E")
elif score<=40:
    print("fail")
else:
    print("default score")  
# p3
num=int(input("enter the number to create a table "))
for i in range(1,11):
      print(num *i)  
      #p4 (using while loop)
i=1;
num1=int(input("enter the number to create a table 1 to 10"))
while(i<=10):
    print(num1*i)
    i+=1;
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    print()
def nofunction():
    pass
#control statements
fruits=['mango','orange','banana','apple','strawberry','cherries']
for f in fruits:
    if(f=='apple'):
        break
    else:
        print(f)
for f in fruits:
    if(f=='apple'):
        continue
    else:
        print(f)
for i in range(51):
    if(i%10==0):
        continue;
    else:
        print(i)
