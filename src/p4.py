'''
'A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome(number):
    "number should be given as string"
    if number[::-1] == number:
        return True
    else:
        return False


def find_largest_palindrome(digits):
    factor1 = "9"*digits    
    result_arr = []
    
    factor1 = int(factor1)
    
    while factor1 > int("1"+"0"*(digits-1)):
        factor2 = 990
        if factor2 > factor1:
            factor2 = factor1 - (factor1 % 11)
        while factor2 > 109:
            if is_palindrome(str(factor1 * factor2)):
                result_arr.append(factor1 * factor2)
            factor2 -= 11
        factor1 -= 1
    result_arr.sort()
    print result_arr[len(result_arr) - 1]
    
find_largest_palindrome(3)