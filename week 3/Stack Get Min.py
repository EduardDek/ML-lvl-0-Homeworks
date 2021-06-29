class Stack:
    def __init__(self):
        self.stack=[]
        self.min = []
        self.minqty = -1
        
    def size(self):
            return len(self.stack)

    def isempty(self):
        if self.size()==0:
            return True
        else:
            return False
        
    def pop(self):
        if self.isempty() == False:
            lastval = len(self.stack)-1
            if self.stack[lastval] == self.min[self.minqty]:
                self.min.pop(self.minqty)
                self.minqty = self.minqty-1
            return self.stack.pop(lastval)
            
    def push(self,i):
            self.stack.append(i)
            if self.size() == 1:
                self.min.append(i)
                self.minqty = self.minqty+1
            elif i <= self.min[self.minqty]:
                self.min.append(i)
                self.minqty = self.minqty+1
            
            return i

    def __iter__(self):
        self.list_Iterator = iter(self(stack))
        return self.list_Iterator

    def __next__(self):
        return next(self.list_Iterator)


    def getmin(self):
        return self.min[self.minqty]
    
mystack = Stack()
mystack.push(8)
print(mystack.getmin())
print(mystack.stack)
print(mystack.min)
mystack.push(1)
print(mystack.getmin())
print(mystack.stack)
print(mystack.min)
mystack.push(1)
print(mystack.getmin())
print(mystack.stack)
print(mystack.min)
mystack.push(4)
print(mystack.getmin())
print(mystack.stack)
print(mystack.min)
mystack.push(-2)
print(mystack.getmin())
print(mystack.stack)
print(mystack.min)
mystack.pop()
print(mystack.getmin())
print(mystack.stack)
print(mystack.min)
mystack.pop()
print(mystack.getmin())
print(mystack.stack)
print(mystack.min)
mystack.pop()
print(mystack.getmin())
print(mystack.stack)
print(mystack.min)
mystack.pop()
print(mystack.getmin())
print(mystack.stack)
print(mystack.min)


