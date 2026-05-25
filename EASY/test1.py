# ==============================================================================
# PROBLEM: Count Negative Numbers in a Sorted Matrix
#
# APPROACH: Top-Right Staircase Search (Linear Time Complexity: O(m + n))
#
# BRIEF DESCRIPTION:
# Because the matrix is sorted in decreasing order both row-wise and column-wise,
# the positive numbers naturally group in the top-left, and the negative numbers 
# group in the bottom-right. 
#
# By starting at the TOP-RIGHT corner of the matrix:
# 1. If the current number is NEGATIVE: Because columns decrease from top to bottom, 
#    every single number underneath it in this column must also be negative.
#    We can count them all instantly (rows_remaining - current_row) and move LEFT.
# 2. If the current number is POSITIVE: Because rows decrease from left to right,
#    every number to its left is even larger/positive. We don't care about them,
#    so we move DOWN to find negatives.
#
# This allows us to trace a "staircase" boundary, skipping most of the matrix!
# ==============================================================================


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c= len(grid[0])
        col =0 
        row =0
        count=0
        while row<r and col<c:
            print("\nscanned  "," row : ",row , " col : ", col , " grid: ",grid[row][col])
            if grid[row][col]<0:
                neg =(r-row)*(c-col)
                print(f"negative numbers found: ",neg)
                count+=neg
                c=col
                print("c reduced to ",c)
                print("count incremented to : ",count)
                row+=1
                col=0
            else:
                if col<c-1:
                    col+=1
                else:
                    row+=1
                    col =0
        return count

sol = Solution()

grid1 = [
    [ 4,  3,  2, -1],
    [ 3,  2,  1, -1],
    [ 1,  1, -1, -2],
    [-1, -1, -2, -3]
]
print(f"Test Case 1 Result: {sol.countNegatives(grid1)} (Expected: 8)")

# Test Case 2: Mix of positives and negatives with an all-negative row
grid2 = [
    [ 3,  2,  1],
    [ 1,  0, -1],
    [-1, -2, -3]
]
print(f"Test Case 2 Result: {sol.countNegatives(grid2)} (Expected: 4)")

# Test Case 3: Grid containing absolutely no negative numbers
grid3 = [
    [5, 4, 3],
    [4, 3, 2],
    [3, 2, 1]
]
print(f"Test Case 3 Result: {sol.countNegatives(grid3)} (Expected: 0)")

# Test Case 4: Grid containing ONLY negative numbers
grid4 = [
    [-1, -2],
    [-3, -4]
]
print(f"Test Case 4 Result: {sol.countNegatives(grid4)} (Expected: 4)")