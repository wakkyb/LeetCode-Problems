def removeElement(nums, val):
    nums[:] = [ele for ele in nums if ele != val]
    return len(nums)
    return nums




