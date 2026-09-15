class stack():
    def __init__(self):
        
        self.stack=[]
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        if(self.isempty()):
            print("stack is empty")
        else:
             return self.stack.pop()
    def isempty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
    def  peek(self):
        if self.isempty():
            print("stack is empty")
        print("The value at top is",self.stack[-1])
    def size(self):
        print("The size of stack is",len(self.stack))
    
s=stack()
s.push(10)
s.push(20)
s.push(30)
s.size()
s.peek()

s.pop()
s.peek()
