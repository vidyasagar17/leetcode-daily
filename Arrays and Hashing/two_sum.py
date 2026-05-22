'''
1. Two Sum
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/description/

Problem:
Given an array of integers nums and an integer target, return the indices
of the two numbers such that they add up to target.
Each input has exactly one solution, and you cannot use the same element twice.
The answer can be returned in any order.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
(Because nums[0] + nums[1] = 2 + 7 = 9)

Approach:
Use a hash map to store each number's index as we go.
For every number, check if (target - number) is already in the map.
If yes, we found the pair. If not, add the current number to the map.

Time Complexity: O(n)
Space Complexity: O(n)
'''

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
