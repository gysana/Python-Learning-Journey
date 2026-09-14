f=open("python.txt","w")
f.write("python is the easiest programming language.")
f.write(" This is my fourth lab ,and we have done basic functions on python.")
f.write("Today we are dealing with file handling.")
f.write("understanding open,write ,append modes")
f.write("This is fun to learn")
f.close()
print("file created successfully")
f=open("python.txt","r")
print(f.read())
f.close()
f=open("python.txt","r")
print(f.readline())
f.close()
f=open("python.txt","r")
print(f.read(30))
f.close()
f=open("python.txt","a")
data=[
    "python has several data types.\n",
    "int used for integers.\n"
]
f.writelines(data)
f.close()
f=open("python.txt","w+")
f.seek(50)
f.close()
#exception in file handling using try and except block:
try:
    a=int(input("enter the value of a"))
    b=int(input("enter the value of b"))
    result=a/b
    print("result",result)
except ZeroDivisionError:
    print("cannot divide by zero")
try:
    f=open("abc.txt","r")
    print(read())
    f.close()
except FileNotFoundError as fs:
    print(fs)
else:
    print("printing file contents")
    f=open("abcd.txt","r")
    data=f.read()
    print(data)
finally:
    print("end of program")

