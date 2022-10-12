# collatz conjecture states:
# applying two arithmetic operations repeatedly will eventually transform any positive integer to 1.
# the two arithmetic operations are : 
# take a number x, apply 3x+1 if it is odd and x/2 if it is even. Continue the operations to the results.
#eventually it will end up in a (4 -> 2 -> 1) loop .
def collatz():
    x = n = int(input("Enter a positive integer:"))
    largest = 4
    steps = 0
    if(x>0):
        while (x!=1):
            if(x%2 == 0):
                x = int(x/2)       #divide by 2 if the number is even
                steps = steps+1
                print(x)
                if(largest < x):
                    largest = x
            else:
                x = (3*x) + 1      #Multiply by 3 and add 1 if the number is odd
                steps = steps+1
                print(x)
                if(largest < x):
                    largest = x
        else:
            print("(4 -> 2 -> 1) loop \n The largest number reached by ",n," was: ",largest,"\nTotal steps : ",steps)
    else:
        collatz()
collatz()        
    