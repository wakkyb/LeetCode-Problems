def plus_one(digits):
    new_list = digits[::-1]
    carry = 1
    for i in range(len(new_list)):
        new_list[i] += carry
        if new_list[i] > 9:
            new_list[i] = 0
        else:
            carry = 0
            break
    if carry == 1:
         new_list.append(1)
    return new_list[::-1]




###################################################################################
#                        Leet Code Difficulty Level = Easy                        #  
#                        Runtime = 14 ms    [ > 73.23%]                           #
#                        Memory = 13.18 MB  [ > 82.04%]                           #
###################################################################################  
