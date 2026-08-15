#list---mutable
things=[1,7,8,'b','g']
friends=['khansa','taqwa','momina','urba','mehreen']
print(friends)
print(friends[1:3])#slicing
print(friends[:])#it will return full list
print(friends[::-1])#this will return in reverse order
print(friends[-2])# this will return element of list from last second
friends.sort()#sorting it alphabetically
print(friends)
friends.reverse()
print(friends)
friends.extend(things)
print(friends)
friends.append("sehar")
print(friends)
print(friends.count("taqwa"))
print(friends.index("khansa"))
f=friends.copy()#simply a copy of friends list
friends.clear()#simply clear friends list
print(friends)
f.remove("g")
print(f)
f[1]="amber"#it overwrites it
print(f)
f.pop()#this will remove last element
print(f)
f.pop(5)#pop with index  that removes that element
print(f)
#list inside a list
l=[[1,2,3],[4,5,6],['a','b',2]]
print(l)
li=[x*2 for x in range(1,4)]
print(li)
#creating a list and then appending # and  such that reversing and sorting both show hash in between
#tuple---immutable collection of data items----slicimg,concatenation,copy
tup=(1,2,3,1,4,5)
tup.count(1)
tup1=(4,5,6)
tup2=tup1+tup
print(sum(tup))
print(max(tup))
print(min(tup))
t=([1,2,3],[5,6])
t[0].append(4)#in tuple we cant append ; we were able to append it as inside tuple there was list; 
print(t)
lang=tuple("python")
a,b,c,d,e,f=lang #unpacking in python
print(a,b,c)
series=[n for n in range(1,11)]
print(series)#for deleting a tuple we use delete
series=tuple(series)#list converted in tuple
#series=series+(10)--->it throws a error as it tuple cant conactenate int;it should be of same type
series1=series+(10,)#---now it tells a compiler 10 is not a int number but it is a an iterable and a collection havcing one element only using comma
print(series1)
l=([1,2,3],[2,3,4])
l[0][1]=5 #modification
print(l)
#learning dictionaries {key:values---this pairs would be unique --->mutable collection of data items}
dc={
    1:"puthon",2:"java",3:"c++",4:"java"
}#it have unique keys values can be same 
print(dc)
dc={
    1:"python",
    2:"toc",
    3:"toc",
    3:"coa"#as keys are unique it willoverwrite key 3 as toc is  two times
}
std={
    "name":"gysana",
    "roll-no":62,
    "sem":"five",
     1:"id"
}
print(std)
print(std.keys())#it will return keys
print(std.values())#this will return values
print(std.items())#it will return dictionary as a list
print(std["name"])
print(std.get("name"))#to get values
std.pop("name")
print(std)
std.popitem()#it will pop the last item
print(std)
s=std.copy()#this will hold copy of dictionary
print(s)
std.update({"sem":"six"})#even in this we can append we can add new key value pairs
print(std)
std["address"]="srinagar"#this will append 
print(std)
print(sorted(std))
print(std)
#set--->mutable collection on data items allows only unique items 
s1={1,3,8,9,7,7}#it will remove duplicates
print(s1)
#create a dict of 10 students and enter their marks,take input from user
d={}
for i in range(1,11):
    m=int(input("enter marks ??"))
    std[i]=m
    





