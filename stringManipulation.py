#greeting message
name=input("enter your name: ")
age=int(input("enter your age: "))
print(f"hello {name} your are {age} years old")
print("hello "+name+"! Your are "+str(age)+" years old" )

#string manupalation
sentence=input("tell me about your skills: ")
lowcase=sentence.lower()
uppercase=sentence.upper()
print(lowcase)
print(uppercase)
replaced=sentence.replace(" ","_")
print(replaced)
stripped=sentence.strip("_")
print(stripped)

#length of string
string=input("enter the string: ")
striped=string.replace(" ","")
length=int(len(striped))
print("Number of Charavcter are in the string (excluding spaces): " +str(length))

#escape sequence
s="Hello \n\tWorld \n This isbackslash: \ "
print(s)