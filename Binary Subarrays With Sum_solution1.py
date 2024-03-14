class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if sum(nums[i:j+1])==goal:
                    count+=1         
        return count
