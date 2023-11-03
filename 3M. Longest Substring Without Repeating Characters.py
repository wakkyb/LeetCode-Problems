def length_longest_sub(in_put):
    check_lst = []
    length_counter = []

#take alphabet from string
#check if it is in check_lst
#if not. then add it.. move to next item in string
#if an element reappears...record this string before the item reappeared
#set new string from previous item appearance +1 index
#repeat
    for alpha in in_put:

        if alpha not in check_lst:
            check_lst.append(alpha)
            length_counter.append(len(check_lst))
        elif alpha in check_lst:
            length_counter.append(len(check_lst))
            index = check_lst.index(alpha)
            check_lst = check_lst[index+1:]
            check_lst.append(alpha)
            continue
    return max(length_counter)