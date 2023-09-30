from django.test import TestCase

# Create your tests here.
# class Solution:
#    def FindMaxSubArray(self, nums:list[int] , k:int) -> int:
#       curr = 0
#       for i in range(k):
#          curr += nums[i]

#       ans = curr

#       for i in range(k, len(nums)):
#          curr += nums[i] - nums[k - 1]
#          ans = max(ans, curr)

#       return ans      
      
         
       
# k=4
# nums = [3,-1,4,12,-8,5,6]
# solution = Solution()
# ans = solution.FindMaxSubArray(nums, k)
# print(ans)