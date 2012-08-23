'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

LIMIT = 20

result = number = 0

while not result:
    number += 20
    result = (lambda x: len([i for i in xrange(2, LIMIT+1) if x % i == 0]) == LIMIT-1)(number)

print "The lowest number divisible by all integers between 1-20 is:", number