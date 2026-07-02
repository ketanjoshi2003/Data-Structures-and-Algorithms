def buy_sel(prices):
    buy = 0
    maxprofit = 0
    
    for sell in range(1,len(prices)):
        if prices[sell] > prices[buy]:
            profit = prices[sell]-prices[buy]
            maxprofit = max(maxprofit, profit)
        else:
            buy = sell
    return maxprofit
    
prices = [7, 1, 5, 3, 6, 4]
print(buy_sel(prices))