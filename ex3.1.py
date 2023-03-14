# cd /home/DanielGamePc/Documents/Non-Github code/338/338A3 && python3 ex3.1.py '[EQUATION]'


import sys


# Define a Node class to be used in a singly-linked list
class Node:
   def __init__(self, data=None, next=None):
       self.data = data
       self.next = next


# Define a Stack class using the singly-linked list implementation
class Stack:
   def __init__(self):
       self.top = None
  
   def push(self, data):
       new_node = Node(data)
       new_node.next = self.top
       self.top = new_node
  
   def pop(self):
       if self.top is None:
           return None
       else:
           popped_node = self.top
           self.top = popped_node.next
           return popped_node.data
  
   def is_empty(self):
       return self.top is None
  
   def peek(self):
       return self.top.data


# Define a function to evaluate the arithmetic S-expression using the stack
def evaluate_expression(expression):
   stack = Stack()
   for token in expression.split(" "):
       hasRb = token.find(")")
       hasLb = token.find("(")
       hasDigit=token[0].isdigit()
       #print(token,hasLb,hasRb,hasDigit)


       if hasLb==0:
           token=token[1:]   # remove (
           stack.push(token)  # operator
       else:
           if (hasDigit):
               if hasRb==1: 
                   stack.push(int(token[:hasRb]))
               else:
                   stack.push(int(token))  # push operand 1 or 2


  


       while hasRb>-1:   #evaluate
           operand2 = stack.pop()
           operand1 = stack.pop()
           operator = stack.pop()
           #print(") DETECTED!",operator,operand1,operand2)


           result = None # define result outside of the if statement
           if operator == "+":
               result = operand1 + operand2
           elif operator == "-":
               result = operand1 - operand2
           elif operator == "*":
               result = operand1 * operand2
           elif operator == "/":
               result = operand1 / operand2
           stack.push(result)


           token=token[hasRb+1:]
           hasRb = token.find(")")




  


     




   return stack.pop()


# Get the expression from the command line argument
expression = sys.argv[1]


# Evaluate the expression and print the result
result = evaluate_expression(expression)
print(result)