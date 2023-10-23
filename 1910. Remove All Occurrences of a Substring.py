# input = two arguments... string and substring
# can use while loop with a FALSE boolean for substring is not in string i.e. loop works until is not condition is False i.e. the substring is present in the string
# use a nested for loop that checks if the substring is in string.. and
#   replaces the substring with blank ...
# maybe or shouldn't use continue after removing the substring....

def str_del(big, small):

    k = len(small)

    while small in big:

        for i in range(len(big) - k + 1):
            win = big[i: i + k]
            if win == small:
               big = big.replace(win, "", 1)
        i -= k

    return big


###################################################################################
#                        Leet Code Difficulty Level = Medium                      #  
#                        Runtime = 16 ms    [ > 60.71%]                           #
#                        Memory = 13.24 MB  [ > 84.52%]                           #
################################################################################### 
