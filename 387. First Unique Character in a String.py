def firstUniqChar(s):
    s_copy = s

    temp_comparison_list = []

    while len(s_copy) >= 1:
        if len(s_copy) == 1:
            global target_char
            target_char = s_copy[0]
            break
        elif len(s_copy) > 1:
            temp_comparison_list.append(s_copy[0])
            s_copy = s_copy[1:]

            if temp_comparison_list[0] not in s_copy:
                target_char = temp_comparison_list[0]
                break

            elif temp_comparison_list[0] in s_copy:
                s_copy = s_copy.replace(temp_comparison_list[0], '')
                temp_comparison_list.pop(0)
    if len(s_copy) == 0:
        return -1
    return s.index(target_char)


                    # start checking for using the element in the list... reverse check... for ele
                    # in list if it is in the string or not....
                    #if found delete all instances from the string as well as from the list..
                    #stop the loop at the first alphabet that is not found in the string...
                    #check for its index in the original string



a = 'aa'

print(firstUniqChar(a))
