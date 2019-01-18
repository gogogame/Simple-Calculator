# Python program to introduce Binary Tree 
# group member
# Saran Leenukul 5901012620126
# Danai Sukjun 5901012630059
# Thanabordee Theparag 5901012630075
'''
Todo
-GUI
-funcion to create new node
'''
import math
from pythonds.basic.stack import Stack
            

# A class that represents an individual node in a 
# Binary Tree
class Node:
  def __init__(self,id = 0,key = 0):
    self.operator = -1
    self.left = None
    self.right = None
    self.val = key
    self.id = id
    
  def calc(self):
  # If only 1 child return the only child
    if self == None:
      if self.operator < 2:
        return 0
  # If 2 child do the parent operator
    if self.operator == 0:
      self.key = self.left + self.right
      return self.key
    elif self.operator == 1:
      self.key = self.left - self.right
      return self.key
    elif self.operator == 2:
      self.key = self.left * self.right
      return self.key
    elif self.operator == 3:
      self.key = self.left / self.right
      return self.key
    elif self.operator == 4:
      self.key = math.pow(self.left,self.right)
      return self.key

  def make_child(self, left, right, operator):
    self.left = left
    self.right = right
    self.operator = operator
    return self.calc()

class BinaryCal:
  math_op = "+-*/^"
  digit = "0123456789"
  def infixToPostfix(self, infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in self.digit:
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
      postfixList.append(opStack.pop())
    return " ".join(postfixList)

  def fill_tree(self, expression):
    # expression is string
    #expression = expression[::-1]
    next = 'right'
    for item in expression:
      if item == ' ':
        continue
      elif item in self.math_op:
        operator = item
      elif (item in self.digit) and (next == 'right'):
        right = item
        next = 'left'
      elif (item in self.digit) and (next == 'left'):
        left = item
        next = 'right'

      #print(item)
    return print(expression)
  


# Test
'''
root = Node()
leaf = Node()
print(root.make_child(3,4,0)) # 3+ 4
print(root.make_child(leaf.make_child(2,5,4),4,0)) # 3+ 4
'''

# Test 2
root2 = Node()
exp = '( 3 - ( 2 * 2 ) * ( 3 / 2 ) ) + ( 1 4 + 1 )'
xp = "3 * ( 1 + 2 ) * 4"
t = BinaryCal()
o = t.infixToPostfix(exp)

print(t.fill_tree(o))

