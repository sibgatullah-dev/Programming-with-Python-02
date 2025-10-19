#Exceptions aren't syntax error so we can work around it easily

def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:# This ZeroDivisionError comes when we try to divide with 0 which isn't possible and can crash program 
        print("Can not divided by zero")
    except TypeError:
        print("Unsupported type in the input")
        
print(div(10,2))
print(div(4,0))
print(div(9,3))
print(div('9',3))