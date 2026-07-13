#HARD CODED
def soln1(nums,target):
    def calc_path(index,current_sum):
        if index==len(nums):
            return 1 if target==current_sum else 0
        
        add_path = calc_path(index+1,current_sum+nums[index])
        sub_path =calc_path(index+1,current_sum-nums[index])

        return add_path+sub_path
    
    return calc_path(0,0)


#OPTIMIZED
def soln2(nums,target):
    total_sum = sum(nums)
    if abs(target)>total_sum:       # 1. If the target is out of bounds of what the array can possibly form.
        return 0
    if (target+total_sum)%2 != 0:   # If (Target + TotalSum) is odd, it's impossible to form integer subsets.
        return 0
    
    new_target = (target+total_sum)//2
    dp=[0]*(new_target+1)
    dp[0] = 1
    for num in nums:
        for j in range(new_target,num-1,-1):
            dp[j]+=dp[j-num]

    return dp[new_target]
 
if __name__ == '__main__':
    nums=[1,1,1,1,1]
    target = 3
    print(soln1(nums,target))
    print(soln2(nums,target))









