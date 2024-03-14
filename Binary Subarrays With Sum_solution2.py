class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        current_sum = 0
        sum_counts = {0: 1}  
        
        for num in nums:
            current_sum += num
            if current_sum - goal in sum_counts:
                count += sum_counts[current_sum - goal]
            sum_counts[current_sum] = sum_counts.get(current_sum, 0) + 1
        
        return count