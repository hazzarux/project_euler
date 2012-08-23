'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

NUMBER1 = 6
NUMBER2 = 10001

def is_prime(n):
    '''check if integer n is a prime'''
    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


def generate_nth_prime_number(n):
    currentCount = 1
    currentNumber = long(2)

    while currentCount < n:
        currentNumber += 1
        if is_prime(currentNumber):
            currentCount += 1
    return currentNumber

print generate_nth_prime_number(NUMBER1)
print generate_nth_prime_number(NUMBER2)