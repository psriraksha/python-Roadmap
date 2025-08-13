'''Basic Dictionary Operations:

Create a dictionary to store information about 5 cities in Karnataka and their famous dishes.
Add a new city and its dish to the dictionary.
Update the dish for Bengaluru.
Remove one city from the dictionary.
Use the keys() method to print all city names in the dictionary.
Use the values() method to print all dishes in the dictionary.
Nested Dictionary Practice (Simple for now):

Create a dictionary to store details of two of your friends, including their names, favorite subject, and favorite food.
Access and print the favorite food of one friend.'''
#new

city={ 
    "mangaluru":"korirotti",
    "bengalore":"momos",
    "udupi":"gollibajje"
}
print(city)

#adding new city
city["mysore"]="masala Dose"
print(f"after adding new city: {city}")

#update city food
city["bengalore"]="biriyani"
print(f"after updating a city food: {city}")

#remove
del city["mangaluru"]
print(f"after remove a city: {city}")

#keys
print(city.keys())

#values
print(city.values())


friend1={
    "name":"raksha",
    "fav_sub":"python",
    "fav_food":"vada"
}

friend2={
    "name":"hashish",
    "fav_sub":"maths",
    "fav_food":"hamburger"
}


print(f"fav_food :{friend1["fav_food"],friend2["fav_food"]}")

