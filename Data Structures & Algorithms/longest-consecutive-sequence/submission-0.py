class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert list to a set for O(1) lookups
        num_set = set(nums)
        longest = 0

        for n in nums:
            # Check if 'n' is the start of a sequence
            if (n - 1) not in num_set:
                length = 0

                # Count how far the sequence goes
                while (n + length) in num_set:
                    length += 1

                # update global max length
                longest = max(length, longest)

        return longest