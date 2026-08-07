class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each number
        # Example: [1,1,1,2,2,3] -> {1: 3, 2: 2, 3: 1}
        count = Counter(nums)

        # Step 2: Create buckets where index = frequency
        # Needs to be Len(nums) + 1 to account for 0-based indexing up to Len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        # Ste 3: Iterate backwards from highest frequency bucket to Lowest
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res