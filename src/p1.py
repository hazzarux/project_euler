'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

LIMIT = 1000

def find_numbers_below(limit):
    numbers = []
    for i in range(1,limit):
        numbers.append(i)
    return numbers
    
def get_multiples(limit,base):
    numbers = find_numbers_below(limit)
    multiples = []
    for n in numbers:
        if n % base == 0:
            multiples.append(n)
    return multiples

all_multiples = multiples_3 = get_multiples(LIMIT, 3)
multiples_5=get_multiples(LIMIT, 5)

for i in multiples_5:
    all_multiples.append(i)

all_multiples=list(set(all_multiples)) #delete identical entries from the list!

def get_sum(multiples):
    sum = 0
    for i in multiples:
        sum = sum + i
    return sum

print get_sum(all_multiples)