a=20
b=3
c="*"

#Logical Operator
print("#Logical Operator")
print(f"a and b greater than 10: {a>10 and b>10}") #and
print(f"atlest one of them is less then 5: {a<5 or b<5}")#or
print(f" a not greater than b: {not(a>b)}")#not
print(c*20)

#bitwise operator
print("#bitwise operator")
print(a&b,a|b,a^b)
print(a<<2)
print(b>>1)
print(c*20)

#comparission operator(using <,>)
print("#comparission operator(using <,>)")
age=19
print('"your are adult" if age is greater than 18: ' + str(age>18 ))
print('" your are minor" if age is less than 18: ' + str(age<18 ))
print(c*20)

#membership operator(in,not in)
print("#membership operator(in,not in)")
string=input("enter the string: ")
print(f"char a is in string : {"a"  in string}")#a in string
print( f" 'python' not found in string: {"python" not in string}")#python not in string


