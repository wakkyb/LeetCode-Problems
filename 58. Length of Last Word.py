def lengthofLastword(s):
    lst = s.split()
    sep = lst[len(lst) -1]
    temp = []
    temp.append(sep)
    count = 0
    for i in sep:
        count += 1
    return count






x = "Hello buttercup"

print(lengthofLastword(x))