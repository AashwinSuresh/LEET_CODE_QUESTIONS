# Problem: Check if Array Is Sorted and Rotated

# Description
# Given an array `nums`, return `true` if the array was originally sorted in non-decreasing order and then rotated some number of positions (including zero). Otherwise, return `false`.

# An array `A` rotated by `x` positions results in an array `B` of the same length such that `B[i] == A[(i+x) % A.length]` for every valid index `i`. The input array may contain duplicate elements.

# Core Intuition
# If we treat the array as a circular loop, a sorted and rotated array can have **at most one "drop"** (a point where an element is strictly greater than the next element, including when wrapping around from the last element back to the first). If there are two or more drops, it is impossible for the array to be a rotated version of a sorted array.

# Complexity
# - **Time Complexity:** O(n) — We traverse the array exactly once.
# - **Space Complexity:** O(1) — We only use a single counter variable.

class Solution(object):


    def check(self, nums):
        n=len(nums)
        count =0
        for i in range(0,n):
            # print(f"comparing if {nums[i]} > {nums[(i+1)%n]}")
            if(nums[i]>nums[(i+1)%n]):
                count+=1
                print("count incremented to : ",count)
            if count>1:
                return False
        return True



obj = Solution()
   
# Test Case 1: True (Sorted and rotated by 3 positions)
nums1 = [3, 4, 5, 1, 2]
print(obj.check(nums1))
# Test Case 2: False (Two drops: 2 > 1 and 4 > 2)
nums2 = [2, 1, 3, 4]
print(obj.check(nums2))

# Test Case 3: True (Already sorted, rotated by 0 positions)
nums3 = [1, 2, 3]
print(obj.check(nums3))

# Test Case 4: True (Contains duplicates, valid rotation)
nums4 = [1, 1, 1]
print(obj.check(nums4))

# Test Case 5: True (Contains duplicates, valid rotation)
nums5 = [2, 2, 3, 4, 1, 2]
print(obj.check(nums5))

# Test Case 6: False (Not sorted, multiple random drops)
nums6 = [6, 10, 6, 4, 11]
print(obj.check(nums6))
