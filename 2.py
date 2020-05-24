stocks = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]

def best_price2(stock):
    lowest_stock = 10300
    n = len(stock)
    result = []
    for i in range(1, n):
        if stock[i] < lowest_stock : 
            lowest_stock = stock[i]
        else : result.append(stock[i] - lowest_stock)
    return max(result)

    
print(best_price2(stocks))