#Nested loops, display a pattern of 90 degree angle pyramid using *

for counter in range (10):
    totalCounter = 0
    print()
    while totalCounter < counter:
        print("*", end=' ')
        totalCounter +=1

print()
#range(a,b,c,) where a is starting value, b is ending value, c is increment/decrement value
for counter in range (10, 0, -1):
    totalCounter = 0
    print()
    while totalCounter < counter:
        print("*", end=' ')
        totalCounter +=1

print()

for counter in range (10, 0, -1):
    totalCounter = 0
    print()
    #counts how many white spaces needs to be placed per line
    if counter < 10:  
        whiteSpace = 10 - counter 
        for spaces in range(whiteSpace):
                print(end='  ') 
    #concatenates *
    while totalCounter < counter: 
        print("*", end=' ')
        totalCounter +=1

print()

for counter in range (10):
    totalCounter = 0
    print()
    if counter < 10:  
        whiteSpace = 10 - counter 
        for spaces in range(whiteSpace):
                print(end='  ')
    while totalCounter < counter: 
        print("*", end=' ')
        totalCounter +=1

print()
