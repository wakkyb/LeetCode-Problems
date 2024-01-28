def lengthofLastword(s):
    lst = s.split()
    sep = lst[len(lst) -1]
    temp = []
    temp.append(sep)
    count = 0
    for i in sep:
        count += 1
    return count






###################################################################################
#                        Leet Code Difficulty Level = Easy                        #  
#                        Runtime = 12 ms    [ > 73.75%]                           #
#                        Memory = 13.36 MB  [ > 82.96%]                           #
###################################################################################  
