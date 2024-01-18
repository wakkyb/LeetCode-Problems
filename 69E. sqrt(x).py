def sqrt(x):
    if x == 0 or x == 1:
        return x
    low, high = 0, x // 2 + 1

    while low <= high:
        mid = (low + high) // 2
        square = mid * mid

        if square == x:
            return mid
        elif square < x:
            low = mid + 1
        else:
            high = mid - 1

    return high


dummy_int = 16

print(sqrt(dummy_int))
