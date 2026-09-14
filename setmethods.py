#sets-->it is unordered
s=set()
s={1,2,3,4,4,5,6,8,2,1,0}
print(s)
for i in s:
    print(i)
print(min(s))
print(max(s))
s.add(10)
s.remove(4)
print(s)
a=s.pop()#it will pop any random element from the list AS set is unordered better is to use remove 
print(a)
s.discard(20)#this is same as remove but one thing is if element doesnt exist it doesnt show an error while remove shows error
d=s.copy()#it simply copies
s.clear()
print(s)
#set operations
g={1,2,3,4}
h={3,4,5,6}
print(g|h)#print union 
print(g.union(h))
print(g&h)
print(g.intersection(h))
print(g-h)
print(g.difference(h))
import module
import module as m
from module import person
module.welcome("lily")
m.welcome("harry porter")
name=person["name"]
print(name)
#strings
text="python programming"
print(text)
print(text[1])
print(text[-1])#this will return last  element
print(text[::-1])#print string in reverse
print(text[1:3])
lang="java"
print(text+" "+lang)#concatenation operation
lang=lang*3 # this will cause repition
print(lang)
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.count("python"))
print(text.find("python"))#this will return index of paticular item
print(text.find("programming"))
print(text.replace("python","java"))#temporary replacing
print(text)#original remains as it is ;strings are immutable
print(text.split())
print(text.split(","))
print(text.swapcase())
print(text.startswith("py"))
print(text.endswith("ing"))
text="abc123"
print(text.isdigit())
print(text.isalpha())
print(text.isalnum())
#f strings--- formatted strings in pythoni
name="gysana"
rno=62
id=5
print("my name is"+name +"and my roll no is",rno)
print(f"my name is{name} and my rno is {rno}")
print(f"sum is{id+rno}")

