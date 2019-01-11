# Software Dev Simple Calculator
# make class Number with attribute? and method?
# Note: Bracket NOT Bracelet RIP ENG

def take_input(string): # convert each string to list contain all string
    ''' Back up plan -> remove the bracket instead'''
    expression = []
    toggle = 0 # Use to find )( and insert * between it
    for char in string:
        if char == ' ': # Skip the space
            continue
        elif char == ')':
            #expression.append(char)
            toggle = 1
        elif char == '(':
            if toggle == 1:
                expression.append('*')
                #expression.append(char)
                toggle = 0
            else:
                pass
                #expression.append(char)
            '''
        elif is_digit(char):
            try:
                if is_digit(i):
                    char = char + i
            except:
                pass
            '''
        else:
            expression.append(char)
            toggle = 0
        i = char
    return expression

def unpack(argv): # use to unpack a list
    a = ''.join(argv)
    return a

def is_digit(var): # check if char is digit
    digit = {"1","2","3","4","5","6","7","8","9","0"}
    return var in digit

def is_operator(var): # check if char is operator
    operator = {"+","-","*","/","^"}
    return var in operator

def cal(num1,num2,operator):
  r = 0 # Store Result of calculation
  if operator == "+":
    r += int(num1) + int(num2)
  elif operator == "-":
    r += int(num1) - int(num2)
  elif operator == "*":
    r += int(num1) * int(num2)
  elif operator == "/":
    r += int(num1) / int(num2)
  elif operator == "^":
    r += int(num1) ** int(num2)
  return(r)



def evaluate(expression, temp = 0): # find operand and do it before and after it
    index = 0
    num1 = []
    num2 = []
    toggle = 'left'
    for item in (expression) :
        item = expression.pop(0)
        if item == int(temp):
            make_true = True
        else:
            make_true = False
        print(item)
        if is_digit(item) or make_true:
            if toggle == 'left':
                num1.append(item)
                print(num1)
            elif toggle == 'right':
                num2.append(item)
                print(num2)

        elif is_operator(item):
            if toggle == 'left':
                toggle = 'right'
                operand = item
            elif toggle == 'right':
                print('doit!')
                expression.insert(0, item)
                toggle = 'left'
                try :
                    temp = cal(''.join(num1) ,''.join(num2) ,operand)
                    num1 = []
                    num2 = []
                    expression.insert(0, str(temp))
                    print(expression)
                    evaluate(expression)
                except Exception as error:
                    print(error)
        #print(item)
        #print(expression)



'''
def find_bracelet(string, priority = 0): # use for loop to find open bracelet
    string = take_input(string)
    char_with_priority = []
    for char in string:
        if char == '(': # create new list with priority raise
            priority += 1
            continue
        elif char == ')': # stop doing and lower priority
            priority -= 1
            continue
        else: # append all but ( )
            try:
                #print(string)
                char_with_priority.append(priority)
            except Exception as error:
                print(error)
    return (char_with_priority)

def calc_by_priority(expression, order):
    toggle = 0
    first = max(order)
    print(first)
    for index, item in enumerate(order):
        print(index, item)
        if item == first:
            toggle += 1
            print(toggle)
        elif toggle == 3:
            a = cal(expression[index],expression[index+1],expression[index+2])
            print(a)
        else:
            toggle = 0
'''


test= ("(3 -(22)(3/2)) + (14 + 1)")
print('Remove space ->',take_input(test))
print(evaluate(take_input(test)))

'''
print(eval(test)) # For testing
'''


# 4 ^ 2 / (2*2) +10)
# 3 -(22)(3/2)) + (14 + 1)
