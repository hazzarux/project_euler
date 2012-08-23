'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

LIMIT = 100

def square_of_the_sum(upperLimit):
    base = sum(range(1,upperLimit))
    #print "Sum of all natural numbers:",base
    #print "Square of the sum:",pow(base,2)
    return pow(base,2)
    
def sum_of_the_squares(upperLimit):
    bases = range(1,upperLimit)
    #print "All natural numbers to square:", bases
    
    result = 0
    
    for b in bases:
        result += pow(b,2)
    #print "Sum of the squares:",result
    return result


print "DiFFERENCE:",square_of_the_sum(LIMIT+1)-sum_of_the_squares(LIMIT+1)