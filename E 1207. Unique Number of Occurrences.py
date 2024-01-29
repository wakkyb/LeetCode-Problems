def uniqueoccurences(arr):
    count_dict = {} #use key value pairs for the elements.. first arrange the array then new entry from list is a new
                    # key and the count is the value of the key... if all keys have a unique value: print true..
    arr = sorted(arr)
    for ele in arr:
        if ele not in count_dict:
            count_dict[ele] = 1
        else:
            count_dict[ele] +=1
    print(count_dict)
    flag = True
    hash_val = dict()
    for keys in count_dict:
        if count_dict[keys] in hash_val:
            flag = False
            break
        else:
            hash_val[count_dict[keys]] = 1
    return flag

A = [1,3,4,3,4,4,3]


print(uniqueoccurences(A))
