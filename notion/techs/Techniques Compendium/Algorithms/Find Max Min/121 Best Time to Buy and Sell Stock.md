# 121. Best Time to Buy and Sell Stock

REASONING ATTEMPT:

This differs from two ptr because you don’t know the target value beforehand. In Two Ptr, you knew the target value AND it’s sorted, thus you knew which ptr to move to try to get closer to it. Here, you wouldn’t know which ptr to move.

---

Reqs:

- Because we don’t need to return the indices, try just storing the profit
- However, we need to calculate the profit of sell_price - buy_price, so we update ONE while looping over the OTHER
    
    [GP- update ONE while looping over the OTHER](../Sliding%20window%2073fde3f31ee04c57a6c0a66768e549cf/GP-%20update%20ONE%20while%20looping%20over%20the%20OTHER%206371074563f0446fb7d86bc67932d3ea.md) 
    
- To update the profit, it needs to be better than the current profit
- set the initial guess of buy_price to the first member
- To update buy_price, if new index (sell_price) is less than buy_price, we found a new low

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for sell in prices:
            if (sell - buy > profit):
                profit = sell - buy
            elif sell < buy:
                buy = sell
        return profit
```