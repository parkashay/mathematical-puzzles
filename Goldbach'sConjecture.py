# Goldbach's Conjecture states that: 
#Any positive even integer greater than 2 can be illustrated as a sum of two prime numbers

def testPrime(x):
    for i in range(2,x):
        if x%i == 0:
            return False            #Beginner note : for-else and if-else are two separate things in python. Here, for-else is used.
    else:
            return True
c = 0
num = int(input("Enter an even number greater than 2 : \n"))
for fnum in range(2,num):
    for snum in range(2,fnum+1):
        if testPrime(fnum) & testPrime(snum):
            if ((fnum + snum) == num):
                print(fnum," + ",snum," = ",num)
                c = c+1
print(c," pair(s) of prime numbers sum up to ",num)
