# Problem Statement: Find Minimum in Rotated Sorted Array

# Difficulty: Medium

# Description:
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
# For example, the array nums = [0,1,2,4,5,6,7] might become:
#   - [4,5,6,7,0,1,2] if it was rotated 4 times.
#   - [0,1,2,4,5,6,7] if it was rotated 7 times.

# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# ---------------------------------------------------------
# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Example 2:
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

# Example 3:
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times (remained unchanged).

# ---------------------------------------------------------
# Constraints:
#   - n == nums.length
#   - 1 <= n <= 5000
#   - -5000 <= nums[i] <= 5000
#   - All the integers of nums are unique.
#   - nums is sorted and rotated between 1 and n times.

# ---------------------------------------------------------


class Solution(object):
    def search(self, nums, target):
        if len(nums) == 0 :
            return -1
        if len(nums) == 1 :
            if(nums[0]==target):
                return 0
            else:
                return -1
        n = len(nums)
        a1 = nums[:n//2]
        a2 = nums[n//2:]
        print("a1 is : " ,a1,"a2 is : ",a2 )
        n1 = len(a1)
        n2 = len(a2)
        pos =0
        if n1>1 and (a1[0]<=a1[n1-1]):
            safe_zone = a1
            d_zone = a2
            print("safe zone is a1 : ",safe_zone , " d zone is : ",d_zone)
        elif n2>1 and (a2[0]<=a2[n2-1]):
            safe_zone = a2
            d_zone =a1
            print("safe zone is a1 : ",safe_zone , " d zone is : ",d_zone)
        else:
            if n1==1: 
                if a1[0] == target  : 
                    print("FOUND IN A1")
                    print("\n pos = 0")
                    return 0
                else :
                    safe_zone = a1
                    d_zone = a2
                    print("safe zone is a1 : ",safe_zone , " d zone is : ",d_zone)

            elif n2==1:
                if a2[0] == target   :
                    print("FOUND IN A2")
                    print("\n pos = 1")
                    return 1
                else:
                    safe_zone = a2
                    d_zone = a1
                    print("safe zone is a1 : ",safe_zone , " d zone is : ",d_zone)

            else:
                return -1
        mid = int(len(safe_zone)//2)
        if safe_zone[0] <= target <= safe_zone[len(safe_zone)-1]:
            if safe_zone[mid] == target:
                print("FOUND IN MID")
                return mid if safe_zone == a1 else len(a1) + mid
            else:
                print("safe_zone passed to function\n\n")
                val=self.search(safe_zone,target)
                if val==-1:
                    return -1
            if safe_zone == a1:
                pos = val
                print("pos = ",pos)
                return pos
            else:
                pos = len(a1)+val
                print("pos : ",pos)
                return pos
                
        else:
            print("d_zone passed to function\n\n")
            val=self.search(d_zone,target)
            if val==-1:
                return -1
            if d_zone == a1:
                pos = val
                print("pos = ",pos)
                return pos
            else:
                pos = len(a1)+val
                print("pos : ",pos)
                return pos



obj = Solution()

#INPUTS

# nums = [4,5,6,7,0,1,2]
# target = 3

# nums = [4,5,6,7,0,1,2]
# target = 1

nums = [3,5,1]
target =1

# nums = [1]
# target =0

# nums =[1,3,5]
# target = 5
pos = obj.search(nums,target)
if pos == -1:
    print("\n\nNOT FOUND\n\n")
else:
    print("\n\nVALUE FOUND AT : \n\n",pos)