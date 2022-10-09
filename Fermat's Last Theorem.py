# Fermat's Last Theorem : 
# No natural numbers x,y and z satisfy the equation x^n + y^n = z^n where n > 2.
n = int(input("Enter value of n : "))
lim = int(input("Enter Limit of execution(eg. enter 100 to test upto the value of z upto 100:\n"))
count = 0
for z in range(1,lim):
    for x in range(1,z):
        for y in range(1,x):
            if(((x**n) + (y**n)) == (z**n)):
                print(x,"^",n," + ",y,"^",n," = ",z,"^",n)
                count = count + 1
if(count == 0):
    print("No solutions for this equation.")
else:
    print(count," soultion(s)."," or you can interchange the positions of x and y values to get ",count*2," solutions.")
    print("ex. 4^2 + 3^2 = 5^2 can also be assumed as a different solution than 3^2 + 4^2 = 5^2")
