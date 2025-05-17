#comparison operators
#equal to / not equal to
name = "Hannatu"

print(name == "Hann")
print(name != "hannatu")

#greater than / greater than or equal to
age = 2
print(age > 10)
print(age >= 2)

#less than / less than or equal to
age = 50
print(age < 100)
print(age <= 20)


#Conditional Statements
#if/else statement with a single block
#response = input("Have to done your assignment?" )

#if response == "yes" :
    #print("Go shawtttttyyyyy")
#else : 
    #print ("Well who is going to do it?")

#if/else with multiple options
temperature = 1
if temperature > 25:
    print("Ice pack !!!")
elif temperature > 15:
    print("Room temperature water")
elif temperature > 10:
    print("Tea or coffee ma'am?")
else:
    print("its freezing yo!")


score = 85
if score >= 70:
    print("C")
elif score >= 80:
    print("B")
elif score>=90:
    print("A")
else:
    print("oh")


#logical operators
is_Sunny = True
is_Warm = False

#and
print(is_Sunny and is_Warm)

#or
print(is_Sunny or is_Warm)

#not
print(not is_Sunny)
print(not is_Warm)

