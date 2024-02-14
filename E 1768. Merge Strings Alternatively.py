def merge_alternatively( word1, word2):
    merged_out = []
    l = 0
    r = 0

    if len(word2) > len(word1):
        big = word2
        small = word1
    else:
        big = word1
        small = word2

    len_difference = len(big) - len(small)


    while (len(word2) <=len(word1)) or (len(word1) <= len(word1)):

        merged_out.append(word1[l])
        merged_out.append(word2[r])
        l += 1
        r += 1
        if l >= min(len(word1), len(word2)):
            break

    if len_difference > 0:
        merged_out.append(big[-len_difference:])

    merged_out = ''.join(merged_out)

    return merged_out

w1 = 'Pakistan'
w2 = 'Jhang'




import time
start_t = time.time()
print(merge_alternatively(w1, w2))
end_t = time.time()

run_t = ((end_t - start_t) * 1000)

print('runtime is: ' + str(run_t) + 'ms')