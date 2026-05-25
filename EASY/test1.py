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

