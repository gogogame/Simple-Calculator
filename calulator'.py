def take_input(string):
    expression = list(string)
    return expression

def is_digit(var):
    digit = {"1","2","3","4","5","6","7","8","9","0"}
    return var in digit

def is_operator(var):
    operator = {"+","-","*","/","^"}
    return var in operator

def find_bracelet(string):
    for char #use for loop to find open bracelet
test= ("2*(3/5)")
print(is_digit("3"))
print(take_input(test))


# 4 ^ 2 / (2*2) +10)
# 3 -(22)(3/2)) + (14 + 1)
