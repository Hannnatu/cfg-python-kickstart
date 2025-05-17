#this module explains variables for strings, numbers and booleans,Operators
#string variable class
string1 = "We can use them in double quotation marks"
string2 = 'Never said the single quotes were bad, lol'
string3 = """Now imagine that we can use
three double quotations 
for multiple lines"""
string4 = '''As if thats not all
you can do same with triple single quotations.
Dont you just love Python.'''
#to print any of the variables we have to call them by:
print(string3)


#numbers variables, for this we have integers and floats
integer1 = 100
float1 = 2.0 #the difference is that floats are decimals
#call variable
print(integer1)


#boolean variables
are_you_lying = True
are_you_lying = False


#Operators Class
#arithimetic operations
#addition
result = 10 +4  
print(result)

#subtraction
result = 22 -6
print(result)

#multiplication 
result = 2 * 22
print(result)

#division
result = 30 / 10
print(result)

#integar division - returns the whole number after division
result = 33 // 2
print(result)

#modulus - returns remainders after division
result = 33 % 2
print(result)

#we also have string operarions also called concatenations
#addition
result = "are " + "you " + "okay?"
print(result)

#multiplication
result = "Hanne " * 3
print(result)


#String Formatting Class
#using the .format() method
name = "Hanne"
age = 16
message = "Her name is {} and she is {} years old".format(name, age)
print(message)

#using the f-string method
message = f"Her name is {name} and she is {age} years old" #used when there are lots of variables
print(message)

#List lesson
mixed_list = ["apple", 2937, "catdog", 1]
print(mixed_list)

fruits = ["lychee", "dragon fruit", "clementine"]
print(fruits)

#printing elements on the console
print(fruits[0])  #will print lychee as index 0 is lychee
print(fruits[-1]) #the last item on the list from behind with -3 being lychee


#adding, replacing and removing elements
#to add we use append, insert and extend
fruits.append("kiwi") #adds item to end of list
print(fruits)

fruits.insert(0, "gurasa") #adds item at index 0(beginning)
print(fruits)

fruits.extend(["apricot", "nectarine"])#adds more than one items to the liist
print(fruits)

#removing items on the list
#fruits.pop() #removes last item on the list
#print(fruits)

#fruits.remove("kiwi") #removes first occurence of this item
#print(fruits)

#fruits.clear() #removes all items from list 
#print(fruits)


#replacing items in a list
fruits[2] = 'orange' #replaces fruits at index0 with agbalz
print(fruits)
