class Solution(object):
    def search(self, nums, target):
        if len(nums) == 0:
            return
        n = len(nums)
        a1 = nums[:n//2]
        a2 = nums[n//2:]
        print("a1 is : " ,a1,"a2 is : ",a2 )
        n1 = len(a1)
        n2 = len(a2)
        pos =0
        if n1>1 and n2>1:
            if(a1[0]<=a1[n1-1]):
                safe_zone = a1
                d_zone = a2
                print("safe zone is a1 : ",safe_zone , " d zone is : ",d_zone)
            elif(a2[0]<=a2[n2-1]) and n2>0:
                safe_zone = a2
                d_zone =a1

                print("safe zone is a1 : ",safe_zone , " d zone is : ",d_zone)
        else:
            if a1[0] == target : 
                print("FOUND IN A1")
                return 0
            elif a2[0] == target :
                print("FOUND IN A2")
                return 1
        mid = int(len(safe_zone)//2)
        if safe_zone[0] <= target <= safe_zone[len(safe_zone)-1]:
            if safe_zone[mid] == target:
                print("found")
                return mid
            else:
                print("safe_zone passed to function\n\n")
                pos += self.search(safe_zone,target)
        else:
            print("d_zone passed to function\n\n")
            pos +=  len(a1)-1
            pos+= self.search(d_zone,target)
        return pos


obj = Solution()
#INPUTS
nums = [4,5,6,7,0,1,2]
target = 0
print(obj.search(nums,target))