import copy
y = 10
def isPalindrome(x):
    z = str(x)
    if z == z[::-1]:
        return True
    else:
        return False



print(isPalindrome(y))
