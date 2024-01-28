import copy
y = 10
def isPalindrome(x):
    z = str(x)
    if z == z[::-1]:
        return True
    else:
        return False



print(isPalindrome(y))


###################################################################################
#                        Leet Code Difficulty Level = Easy                        #  
#                        Runtime = 31 ms    [ > 88.77%]                           #
#                        Memory = 13.3 MB   [ > 38.56%]                           #
################################################################################### 
