"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
from itertools import combinations
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for pair in combinations(nums, 2):
            if pair[0]+pair[1]==target:
                if pair[0] == pair[1]:
                    return nums.index(pair[0]), nums.index(pair[1], nums.index(pair[0])+1)
                else:
                    return nums.index(pair[0]), nums.index(pair[1])
                
