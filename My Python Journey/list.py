print("**Lists operation**")
item=["bread","butter","milk","egg","jam"]

#add
print("given list: " +str(item))
append=item.insert(1,"coffe")#2nd pos
append=item.append("cake")#at end
print(f"after appending item at end and second postion: {item}")

#delete
remove=item.pop(1)
print(f"after removing 2nd item from list: {item}")
print("*******************************************")
list=[10,90,60,40,30,29]
print("given list: "+ str(list))
list.sort()#sorting
list.reverse() #reverse
print(f"Descending order: {list}")
list.reverse()#reverse
print(f"reversed list: {list}")


