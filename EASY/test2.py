# Problem: Minimum Element After Digit Sum Replacements

# Description:
# You are given an integer array 'nums'.
# You replace each element in 'nums' with the sum of its digits.
# Return the minimum element in 'nums' after all replacements have been made.class Solution:

class Solution:
    def minElement(self, nums: list[int]) :
        minimum = float('inf')
        for num in nums:
            d_sum = 0
            while num>0:
                d_sum+= num%10
                num = num//10
            if d_sum < minimum : 
                minimum = d_sum
        return minimum

# Instantiate the solution class
sol = Solution()

# Test Case 1: Standard case with mixed digit lengths
nums1 = [10, 12, 13, 14]
print(f"Input: {nums1} -> Output: {sol.minElement(nums1)}")  
# Expected Output: 1 (Sums are [1, 3, 4, 5], min is 1)

# Test Case 2: Array already consists of single-digit minimums
nums2 = [1, 2, 3, 4]
print(f"Input: {nums2} -> Output: {sol.minElement(nums2)}")  
# Expected Output: 1 (Sums are [1, 2, 3, 4], min is 1)

# Test Case 3: Large numbers where smaller numbers have larger digit sums
nums3 = [999, 19, 199]
print(f"Input: {nums3} -> Output: {sol.minElement(nums3)}")  
# Expected Output: 10 (Sums are [27, 10, 19], min is 10)

# Test Case 4: Single element array
nums4 = [456]
print(f"Input: {nums4} -> Output: {sol.minElement(nums4)}")  
# Expected Output: 15 (Sum of 4+5+6 = 15)        