import time
start_time = time.time()
x = [4, 7, 4, 8, 9, 9, 9, 10, 20, 10, 10, 10, 10, 10, 9, 9, 9]

def majorityElement(nums):
    thresh = len(nums)/3
    elements_dict = {}
    for element in nums:
        if element in elements_dict:
            elements_dict[element] += 1
        else:
            elements_dict[element] = 1
    selected = []
    for key, value in elements_dict.items():
        if value > thresh:
            selected.append(key)
    return selected

print(majorityElement(x))

for i in range(1000000):
    pass
end_time = time.time()
print(f"The runtime of the code is {(end_time - start_time) * 1000} ms.")
