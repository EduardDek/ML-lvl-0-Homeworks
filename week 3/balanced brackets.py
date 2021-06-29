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


    def last(self):
        return self.stack[self.size()-1]

    def penult(self):
        return self.stack[self.size()-2]           


ptdict = {"[" : "]",
          "(" : ")",
          "{" : "}",
          "<" : ">"}    
mystack = Stack()
txt = "int main() {\n\tfor (int i = 0; i < 10; ++i) {\n\t\t//some code\n\t}\n}\n}"

for x in txt:
    if x in ptdict or x in ptdict.values():
        mystack.push(x)
        if mystack.size()>1:
            if x == ptdict.get(mystack.penult()):
                mystack.pop()
                mystack.pop()

if mystack.size()==0:
    print ("Brackets are Balanced")
else:
    print ("Brackets are not Balanced")


