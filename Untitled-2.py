stocks = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
def best_price(stock) : 
    result = []
    for i in range(len(stock)-1) :
        for j in range(i+1, len(stock)) :
            result.append(stock[j] - stock[i])
    # return result
    return max(result)

print(best_price(stocks))    