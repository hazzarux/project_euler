'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

NUMBER = 10001


def isPrime(p):
    if(p==2): return True
    if(not(p&1)): return False
    return pow(2,p-1,p)==1

def generate_prime_number(n):
    currentCount = 1
    currentNumber = long(2)
    while currentCount < n:
        currentNumber += 1
        if isPrime( currentNumber ):
            currentCount += 1
    return currentNumber

print generate_prime_number(NUMBER)