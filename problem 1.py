"""
For a given positive number num, identify the palindrome formed by performing the following operations-

1. Add num and its reverse
2. Check whether the sum is palindrome or not. If not, add the sum and its reverse and repeat the process until a palindrome is obtained
"""
def check_palindrome(num):
    rev_num = num[::-1]
    if num == rev_num:
        print(num)
    else:
        num = int(num)
        rev_num = int(rev_num)
        num+=rev_num
        check_palindrome(str(num))

num = input()
check_palindrome(num)