class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.splitAndFind(prices,0,len(prices) - 1)
    
    def splitAndFind(self, prices, left, right):
        if left>= right:
            return 0
        profit = 0
        mid = (left + right) // 2
        leftProfit = self.splitAndFind(prices, left, mid)
        rightProfit = self.splitAndFind(prices, mid+1, right)
        calProfit = self.compareAndFind(prices, left, mid, right)
        profit = max(profit, max(calProfit, max(leftProfit,rightProfit)));
        return profit
    
    def compareAndFind(self, prices, left, mid, right):
        minStock = prices[left]
        for i in range(left+1, mid+1):
            minStock = min(minStock, prices[i])
        
        maxStock = 0
        for i in range(mid+1, right+1):
            maxStock = max(maxStock, prices[i])
        return maxStock - minStock
