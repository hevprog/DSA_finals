#stack 
import random

class stack:
    def __init__(self):
        self.element = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.stack = []
        self.random = random.sample(self.element, 5)
        self.stack.append(self.random)

    def showStack(self):
        print(self.stack)
    
    def push(self):
        self.random = random.sample(self.element, 1)
        if(len(self.stack) < 7):
            self.stack.append(self.random)
        else:
            print("STACK IS FULL")
            
    def pop(self):
        if(len(self.stack) > 0):
            self.stack.pop()
        else:
            print("STACK IS EMPTY")
            
    def peek(self):
        if(len(self.stack) > 0):
            top = stack[-1]
        else:
            print("STACK IS EMPTY")
    
    def isEmpty(self):
        isEmpty = not bool(stack)

    def size(self):
        print("Size: ",len(stack))
            
        
if __name__ == "__main__":
    s = stack()

    s.push()
    s.showStack() 
        
        
        


    

        
        
        
        
        
