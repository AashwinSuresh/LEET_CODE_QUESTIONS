# # LeetCode 955: Delete Columns to Make Sorted II (Medium)

# ## Problem Description
# Given an array of $n$ strings `strs` of equal length, determine the minimum number of columns to delete so that the final array of strings is sorted in lexicographical (alphabetical) order from top to bottom ($strs[0] \le strs[1] \le \dots \le strs[n-1]$).

# ## Key Concept
# Unlike LeetCode 944, columns do not need to be sorted independently. Leftmost columns carry higher sorting weight. Once a column strictly establishes that $strs[i] < strs[i+1]$, the characters to the right of that column do not matter for those specific rows. We use a greedy approach to evaluate columns from left to right, maintaining a record of which rows are already securely sorted.

# - **Time Complexity:** $O(N \times M)$ where $N$ is the number of strings and $M$ is the string length.
# - **Space Complexity:** $O(N)$ to track row-sorting states.



class Solution(object):

    def check_strs(self,temp,is_sorted):
        for i in range(len(temp)-1):
            if(not is_sorted[i] and temp[i] > temp[i+1] ):
             return 0
        return 1   
    def minDeletionSize(self, strs):
        deletions =0
        rows =len(strs)
        is_sorted = [False]*(rows-1)
        for i in range(len(strs[0])):
            current_col = [s[i] for s in strs]
            flag = self.check_strs(current_col,is_sorted)
            
            if(flag == 0):
                deletions+=1 
            else:
                for i in range(rows-1):
                    if(current_col[i]<current_col[i+1]):
                        is_sorted[i] = True
            
        return deletions



obj = Solution()

strs= ["zyx","wvu","tsr"]
print("NUMBER OF DELETIONS FOR STRING ",strs,"  : ",obj.minDeletionSize(strs))


strs= ["ca","bb","ac"]
print("NUMBER OF DELETIONS FOR STRING ",strs,"  : ",obj.minDeletionSize(strs))


strs=["xga","xfb","yfa"]
print("NUMBER OF DELETIONS FOR STRING ",strs,"  : ",obj.minDeletionSize(strs))
