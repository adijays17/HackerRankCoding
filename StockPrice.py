def maxProfit(prices):
    if not prices:
        return 0
    mx = prices[0]
    mn = prices[0]
    revert = False
    old_mx = mx
    old_mn = mn
    for i in range(1, len(prices)):
        if prices[i] < mn:
            if mx - mn > old_mx - old_mn:
                old_mx = mx
                old_mn = mn
            mn = prices[i]
            mx = prices[i]
            revert = True
        if prices[i] > mx and prices[i] - mn > old_mx - old_mn:
            old_mx = mx
            mx = prices[i]
            revert = False
    if revert:
        return old_mx - old_mn
    else:
        return mx - mn
print(maxProfit([1,2,3,4,5,6,7]))
