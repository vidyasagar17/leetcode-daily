"""
LeetCode 4: Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/

Given two sorted arrays nums1 and nums2 of size m and n, return the
median of the two sorted arrays. The overall run time complexity
should be O(log(m + n)).

Example:
    Input:  nums1 = [1,3], nums2 = [2]
    Output: 2.00000           (merged = [1,2,3], median = 2)

    Input:  nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000           (merged = [1,2,3,4], median = (2+3)/2)

Time:  O(log(min(m, n)))
Space: O(1)
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Binary search over the smaller array to keep it O(log(min(m, n)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2
        lo, hi = 0, m

        while lo <= hi:
            i = (lo + hi) // 2          # cut in nums1
            j = half - i                # matching cut in nums2

            left1 = nums1[i - 1] if i > 0 else float("-inf")
            right1 = nums1[i] if i < m else float("inf")
            left2 = nums2[j - 1] if j > 0 else float("-inf")
            right2 = nums2[j] if j < n else float("inf")

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2:
                    return float(max(left1, left2))
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                hi = i - 1
            else:
                lo = i + 1
