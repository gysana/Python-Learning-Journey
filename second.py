score=float(input("enter your score"))
if score>90 and score<=100:
    print("grade A")
elif score>80:
    print("grade B")
elif score>70:
    print("grade C")
elif score>60:
    print("grade D")
elif score>=50:
    print("grade E")
elif score<=40:
    print("fail")
else:
    print("default score")
#ternary operator  a if a>b else b;
a=15
b=10
result=a if a>b else b;
#mytuple=("gysana",1,2.5,'python')--->immutable
tup=('a','b','c')
tup*2
tup+('d','f')#---concatenation
tup[1:2]#-----slicing
dic={1:'gysana',2:'anupriya'}#---->dictionary mutable
dic1={'name':'gysana',1:[1,2,3]}
len(dic1)
dic1.key()#--->return list of keys
dic1.values()#---->list of values 
set={1,2,3,4,5,6}#--->it will always store unique elements not store duplicates
s1={1,2,3}
s2={4,5,6}#union,intersection,difference

