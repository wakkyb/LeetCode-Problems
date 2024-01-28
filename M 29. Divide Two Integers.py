def divide( dividend, divisor):

    if dividend == divisor:
        return 1
    
    elif dividend > divisor and dividend > 0 and divisor > 0: #both ints are positive and dividend is greater than divisor e.g. 7/3
        count_positive_both = 0
        remainder = dividend - divisor

        while remainder >= 0:
            remainder = dividend - divisor
            count_positive_both +=1
            dividend = remainder
            if remainder < divisor:
                break
        return count_positive_both

    elif dividend < divisor and dividend > 0 and divisor > 0: #both ints are positive and dividend is smaller than divisor e.g. 3/7... simply return 0
        return 0

    elif dividend < 0 and divisor < 0 and dividend > divisor: #dividend and divisor negative and dividend greater than divisor e.g. -3/-7
        return 0


    elif dividend > 0 and divisor < 0: #dividend is positive and divisor is negative e.g. 7/-3
        divisor_2_pos = divisor * -1
        count_negative_divisor = 0
        remainder = dividend - divisor_2_pos

        while remainder >= 0:
            remainder = dividend - divisor_2_pos
            count_negative_divisor += 1
            dividend = remainder
            if remainder < divisor_2_pos:
                break
        return count_negative_divisor * -1

    elif dividend < 0 and divisor > 0: #dividend is negative and divisor is positive e.g. -7/3
        dividend_2_pos = dividend * -1
        count_negative_dividend = 0
        remainder = dividend_2_pos - divisor

        while remainder >= 0:
            remainder = dividend_2_pos - divisor
            count_negative_dividend += 1
            dividend_2_pos = remainder
            if remainder < divisor:
                break
        return count_negative_dividend * -1


    elif dividend < 0 and divisor < 0: #both ints are negative e.g. -7/-3
        count_negative_both = 0
        remainder = dividend + divisor

        while remainder <= 0:
            remainder = dividend - divisor
            count_negative_both += 1
            dividend = remainder
            if remainder > divisor:
                break
        return count_negative_both

a = 7
b = -3

print(divide(a,b))

