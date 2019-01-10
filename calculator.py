# Software Dev Simple Calculator
# make class Number with attribute? and method?
expression = []
def take_input(string): # convert each string to list contain all string
    for char in string:
        if char == ' ': # Skip the space
            continue
        else:
            expression.append(char)
    return expression

def unpack(argv): # use to unpack a list
    return argv

def is_digit(var): # check if char is digit
    digit = {"1","2","3","4","5","6","7","8","9","0"}
    return var in digit

def is_operator(var): # check if char is operator
    operator = {"+","-","*","/","^"}
    return var in operator

def put_in_bracelet(string, priority): # group sererate bracelet with priority list
    pass

def find_bracelet(string, priority = 0): # use for loop to find open bracelet
    for char in string:
        if char == '(': # create new list with priority raise
            priority += 1
            continue
        elif char == ')': # stop doing and lower priority
            priority -= 1
            continue
        else: # append all but ( )
            try:
                b = list(char)
                print(char)
                b.append(priority)
            except Exception as error:
                print(error)



test= ("(3 -(22)(3/2)) + (14 + 1)")
print('Remove space ->',take_input(test))
find_bracelet(take_input(test))
'''
print(eval(test)) # For testing
'''


# 4 ^ 2 / (2*2) +10)
# 3 -(22)(3/2)) + (14 + 1)
