accounts = [[2,8,7],[7,1,3],[1,9,5]]

def maximumwealth(x):
    max_wealth = 0
    compare_list = []
    for i in x:
        customer_wealth = sum(i)
        compare_list.append(customer_wealth)
    max_wealth = max(compare_list)
    return max_wealth

print(maximumwealth(accounts))
