def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums = sorted(nums)
        return nums.index(target)

a = [1, 2, 3, 4, 5]
b = 0
print(searchInsert(a, b))
