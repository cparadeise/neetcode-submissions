class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       # Initialize the left pointer (buy day) and right pointer (sell day)
        l, r = 0, 1
        max_p = 0  # Track maximum profit
        
        # Scan through the array until the right pointer reaches the end
        while r < len(prices):
            # Is this a profitable transaction?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_p = max(max_p, profit)
            else:
                # We found a new lowest price to buy!
                # Shift the left pointer directly to where the cheaper price is
                l = r
                
            # Always move the right pointer forward to check the next day
            r += 1
            
        return max_p