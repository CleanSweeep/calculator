import math
print("[][][][][][][][][]][][][][][][][][][][][][][][][][][][]")
print("[]---------------------------------------------------[]")
print("[]                 Calculator                        []")
print("[]---------------------------------------------------[]")
print("[][][][][][][][][]][][][][][][][][][][][][][][][][][][]")
try:
    a=float(input("Enter a number: "))
except:
    print("Invalid input")
print("If you want to add both the numbers type \"+\"")
print("If you want to subtract both the numbers type \"-\"")
print("If you want to multiply both the numbers type \"*\"")
print("If you want to divide both the numbers type \"/\"")
print("If you want to get the remainder type \"%\"")
print("If you want to get the exponential of the number type \"^\"")
print("If you want to do the square root type \"sq\", also ignore the second number")
c=input("Enter one of the following signs: ")
b=float(input("Enter another number: "))
if c == "+" :
    sum=(a)+(b)
    print(sum)
elif c == "-" :
    difference=(a)-(b)
    print(difference)
elif c == "*" :
    product=(a)*(b)
    print(product)
elif c == "/" :
    divide=(a)/(b)
    print(divide)
elif c == "%" :
    mod=(a)%(b)
    print(mod)
elif c == "sq" :
    sqrte=(math.sqrt(a))
    print(sqrte)
elif c == "^":
    exp=(a)**(b)
    print(exp) 
else:
    print("Invalid sign")