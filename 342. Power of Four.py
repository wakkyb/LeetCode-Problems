import time
start_t = time.time()

def isPowerOfFour(n):
    print(n ** (1 / 4))

    if (n**(1/4)) % 1 == 0:
        return True
    else:
        return False


a = 5
print(isPowerOfFour(a))

end_t = time.time()

e_t = (end_t - start_t) *1000

print(e_t, 'ms')