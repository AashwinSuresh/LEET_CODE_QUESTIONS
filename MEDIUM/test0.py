# # LeetCode 955: Delete Columns to Make Sorted II (Medium)

# ## Problem Description
# Given an array of $n$ strings `strs` of equal length, determine the minimum number of columns to delete so that the final array of strings is sorted in lexicographical (alphabetical) order from top to bottom ($strs[0] \le strs[1] \le \dots \le strs[n-1]$).

# ## Key Concept
# Unlike LeetCode 944, columns do not need to be sorted independently. Leftmost columns carry higher sorting weight. Once a column strictly establishes that $strs[i] < strs[i+1]$, the characters to the right of that column do not matter for those specific rows. We use a greedy approach to evaluate columns from left to right, maintaining a record of which rows are already securely sorted.

# - **Time Complexity:** $O(N \times M)$ where $N$ is the number of strings and $M$ is the string length.
# - **Space Complexity:** $O(N)$ to track row-sorting states.


class Solution(object):

    def check_strs(self,strs):
        for i in range(len(strs)-1):
            if(strs[i] > strs[i+1] ):
                return 0
        return 1
    def minDeletionSize(self, strs):
        k=1
        temp = strs
        deletions =0
        for i in range(len(strs[0])):
            flag = self.check_strs(strs)
            
            
            if(flag == 0):
                for j in range(len(strs)):
                    temp[j] = strs[j][k:]
                k+=1
                strs = temp 
                deletions+=1
                print(strs)
            else:
                print("lexicographically correct string : ",strs)
                return deletions


obj = Solution()
strs = ["ca","bb","ac"]
print("NUMBER OF DELETIONS  : ",obj.minDeletionSize(strs))


# this is the main branch , currently it doesnt have any things from the temp branch
# but it will be later merged to the main branch