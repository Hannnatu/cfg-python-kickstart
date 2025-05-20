#Iteration - i is iteration value
#FOR loops lesson
#for i in range(10):
    #print(i) #code being executed on each run

total = 2

for number in range(5):
    print(number)
    print(f'current total: {total}')
    total = total + number
    print(f'new total: {total}')


#WHILE loops lesson
x = 0
#while x < 5:
    #print(x)
    #x += 1 #this increases x by 1 each time of execution

#countdown = 7
#while countdown > 6:
    #print(countdown)
   # countdown = countdown - 1 #the modifier

#controlling flow of loops
#break : early loop termination

for i in range(4):
    if i == 2:
        break
    print(i)


#continue: skips current itration
for i in range(9):
    if i == 9:
        continue
    print(i)







