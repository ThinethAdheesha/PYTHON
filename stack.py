class stack:
    def __init__(self,capacity):
         self.max_capacity = capacity
         self.list=[]

    def __str__(self):
         return str(self.list) 

    def isempty(self):
         if self.list == []:
            return  True 
         else: 
             return False  
    def isfull(self):
        return len(self.list) == self.max_capacity
         
    def pushi(self,value):
        if self.isfull():
           return "this stack is full"
        else:
            return self.list.append(value)
    def push(self,value):
        return self.list.append(value)     
    def peek(self):
        if self.isempty():
            return "stack is empty"
        else:
            return self.list[-1]
    def pop(self):
        if self.isempty():
             return "stack is empty"
        else:
               return  self.list.pop()

        
    
ex =stack(3)
ex.pushi(30)
ex.pushi(40)
ex.pushi(10)
ex.pushi(25)

print(ex)
print(ex.pushi(40))