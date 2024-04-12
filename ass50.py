"""
get a list a = [2,3,4,55,33,4,55,343,66,77,88,99] and write a program to find list of non adjacent numbers of every number.

"""

class Solution:
   def solve(self, nums):
      if len(nums) <= 2:
         return max(nums)
      noTake = 0
      take = nums[0]
      for i in range(1, len(nums)):
         take, noTake = noTake + nums[i], max(noTake, take)
         return max(noTake, take)
ob = Solution()
nums = [3, 5, 7, 3, 6]
print(ob.solve(nums))