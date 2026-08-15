def max(n1,n2,n3):#formal parameters
    if n1>n2 and n1>=n3:
        return n1
    elif n2>=n3 and n2>=n1:
        return n2
    else:
        return n3
result=max(40,20,30)#actual parameters
print(result)
def swap(a,b):
    c=a
    a=b
    b=c
result=swap(3,4)
def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
result=swap(5,6)
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

si = (p * r * t) / 100

print("Simple Interest =", si)
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

print("BMI =", bmi)
days = int(input("Enter number of days: "))

years = days // 365
remaining_days = days % 365
weeks = remaining_days // 7

print("Years =", years)
print("Weeks =", weeks)
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

print("Bitwise AND =", a & b)
print("Bitwise OR =", a | b)
print("Bitwise XOR =", a ^ b)
print("Bitwise NOT of a =", ~a)
print("Bitwise NOT of b =", ~b)
