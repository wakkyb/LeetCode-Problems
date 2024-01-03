def strStr(haystack, needle):
    for i in range(len(haystack) - len(needle) +1):
        global count
        count = 0
        if haystack[i : i+len(needle)] == needle:
            count +=1
            return i
    if count == 0 or len(needle) > len(haystack):
        return -1

A = "sabutsad"
B = "dat"

print(strStr(A, B))