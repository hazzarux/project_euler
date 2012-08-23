'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

#NUMBER = 13195
NUMBER = 600851475143

def prime_factors(n):
    factors = []
    lastresult = n
    
    # 1 is a special case
    if n == 1:
        return [1]
    
    while 1:
        if lastresult == 1:
            break
        c = 2
        while 1:
            if lastresult % c == 0:
                break
            c += 1
        factors.append(c)
        lastresult /= c
    return factors

print max(prime_factors(NUMBER)) #find largest prime number! max!