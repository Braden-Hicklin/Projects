# This program serves as a comprehensive and unique way solve a basic arithmetic equation by 
# taking a string input from the user and solve said equation following basic operational 
# rules like PEMDAS. 

# Date of Completion: 7/20/2023
# Author: Braden Hicklin

# For all up to operations:
# float, float --> float
def Add(a, b):
    return a + b

def Subtract(a, b):
    return a - b

def Multiply(a, b):
    return a * b
    
def Divide(a, b):
    return b / a

def Power(a, b):
    return b ** a

# Detects if the current element is a mathematical operator
# If element is an operator, then function returns False
# int --> bool
def Operations(element):
    operations = ['(',')','^','*','/','+','-','_','a']
    if (element in operations):
        return False
    else:
        return True
    
# Deletes all instances of manually created spaces
def RemoveSpaces(li):
    newLi = [i for i in li if i != "_"]
    return newLi

# Grabs the numbers in the list based on the input direction, used to combine numbers not separated by operations
# list, string --> list
def Collect(li, direction):
    newLi = []
    index = li.index("a") +1
    if direction == "next":
        for x in range(index, len(li)):
            if (Operations(li[x])):
                newLi.append(li[x])
            else:
                break
    if direction == "prev":
        li.reverse()
        index = li.index("a") +1
        for x in range(index, len(li)):
            if (Operations(li[x])):
                newLi.append(li[x])
            else:
                break
        li.reverse()
        newLi.reverse()
    newLi = ''.join(newLi)
    return newLi

# Replaces already calculated components with "_" to be removed via RemoveSpaces function
# list, string --> list
def CutFromLi(li, direction):
    if direction == "next":
        index = li.index("a") +1
        for x in range(index, len(li)):
            if (Operations(li[x])):
                li[x] = "_"
            else:
                break
    if direction == "prev":
        li.reverse()
        index = li.index("a") +1
        for x in range(index, len(li)):
            if (Operations(li[x])):
                li[x] = "_"
            else:
                break
        li.reverse()
    return li

# Performs the operation specified by variables
# Receives a list, a string for the operation, and the function name based on the operation, returns a list
# list, string, function --> list
def MathBlock(li, op, fun):
    i = li.index(op)
    li[i] = "a"
    item1 = float(Collect(li, "next"))
    item2 = float(Collect(li, "prev"))
    item3 = str(fun(item1, item2))
    li = CutFromLi(li, "next")
    li = CutFromLi(li, "prev")
    li[i] = item3
    print(item1, op, item2, "=", item3)
    li = RemoveSpaces(li)
    return li

# Performs a calculation within the parentheses separate from the main equation
# list --> list
def Para(mainLi):
    li = []
    num = 0
    start = 0
    end = 1
    while start != end:
        for x in range(len(mainLi)):
            if mainLi[x] == "(":
                start = x + 1
            if mainLi[x] == ")":
                end = x
                break
        for x in range(start, end):
            li.append(mainLi.pop(x))
            break
    num = FinCalc(li)
    i = mainLi.index("(")
    j = mainLi.index(")")
    if (Operations(mainLi[i-1])):
        mainLi[i] = "*"
        mainLi[j] = num
    else:
        mainLi[i] = num
        del mainLi[j]
    return mainLi

# Performs main calculation by combining each of the previously initialized functions
# list --> float
def FinCalc(li):
    while len(li) != 1:
        if "(" in li:
            li = Para(li)
        elif "^" in li:
            li = MathBlock(li, "^", Power)
        elif "*" in li and "/" in li:
            if li.index("*") < li.index("/"):
                li = MathBlock(li, "*", Multiply)
            elif li.index("*") > li.index("/"):
                li = MathBlock(li, "/", Divide)
        elif "*" in li:
            li = MathBlock(li, "*", Multiply)
        elif "/" in li:
            li = MathBlock(li, "/", Divide)
        elif "+" in li:
            li = MathBlock(li, "+", Add)
        elif "-" in li:
            li = MathBlock(li, "-", Subtract)
    return li[0]


# Driver Code
def main():
    Equation = input("Input an Equation: ")
    Equation.replace(" ", "")
    eqLi = []
    for x in Equation:
        eqLi.append(x)
    print(Equation, " = " , FinCalc(eqLi))

if __name__=="__main__":
    main()