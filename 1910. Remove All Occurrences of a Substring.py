import copy
# input = two arguments... string and substring
# can use while loop with a FALSE boolean for substring is not in string i.e. loop works until is not condition is False i.e. the substring is present in the string
# use a nested for loop that checks if the substring is in string.. and
#   replaces the substring with blank ...
# maybe or shouldn't use continue after removing the substring....

def str_del(big, small):
    shadowc = copy.deepcopy(big)

    k = len(small)

    while small in shadowc:

        for i in range(len(shadowc) - k + 1):
            win = shadowc[i: i + k]
            if win == small:
               shadowc = shadowc.replace(win, "", 1)

    return shadowc
