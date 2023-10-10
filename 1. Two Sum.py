# input ==> an array
# Output ==> indices of the two numbers whose sum = target


nums = [2,7,11,15]
final = 9

def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        if target - num in num_to_index:
            return [num_to_index[target - num], i]
        num_to_index[num] = i
    return []



###################################################################################
#                        Leet Code Difficulty Level = Easy                        #  
#                        Runtime = 35 ms    [ > 87.67%]                           #
#                        Memory = 13.5 MB   [ > 78.77%]                           #
################################################################################### 
