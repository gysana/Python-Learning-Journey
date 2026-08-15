from functools import reduce
#recursions in python
#lamda functions : small,anonymous,one-shot operation functions
# syntax ----lamda variables:expression
sum=lambda x,y:x+y # instead of using function lamda is easier in syntax
print(sum(3,4))
average=lambda x,y,z:(x+y+z)/3
print(average(3,4,5))# we usually use it with higher order functions like map(),reduce (),filter()
#map(function,iteration)
l=[2,3,5,7,8,10,12]
lis=map(lambda x:x*2,l)
print(list(lis))
#filter:filter(predicate,iterable)--it will return list which holds true on predicate
age=[12,34,56,89,44,55,3,10]
result=filter(lambda x:x>=18,age)
print(list(result))
even=[2,5,18,7,6,8]
res=filter(lambda x:x%2==0,even)
print(list(res))
#reduce functtion:one number or result at the end----syntax reduce(function,iterator)
num=[2,5,18,7,6,8]
n=reduce(lambda x,y:x+y,num)
print(n)