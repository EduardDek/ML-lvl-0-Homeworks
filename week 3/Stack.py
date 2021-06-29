class Stack:
    def __init__(self, *args):
        self.stack=[]
        for i in args:
            self.stack.append(i)


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
            return self.stack.pop(lastval)
            
    def push(self,i):
            self.stack.append(i)
            return i

    def __iter__(self):
        self.list_Iterator = iter(self(stack))
        return self.list_Iterator

    def __next__(self):
        return next(self.list_Iterator)        



    
mystack = Stack(3,5)
mystack.pop()
mystack.push(8)
print(mystack.stack)
print(mystack.size())
