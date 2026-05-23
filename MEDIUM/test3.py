import heapq

#  A SOMEWHAT OPTIMIZED CODE
class Solution1:
    def maximumHappinessSum1(self, happiness, k) :
        max_heap =[-s for s in happiness]
        heapq.heapify(max_heap)
        total_happiness = 0
        for i in range(0,k):
            m =-heapq.heappop(max_heap)
            if (m-i)>0 :
                current_val = m - i 
            else:
                break
            total_happiness+=current_val
            print("CURRENT VALUE : ",current_val , " TOTAL_HAPPINESS : ",total_happiness)
        return total_happiness
       

 #MAX_OPTIMIZATION 
class Solution2:
    def maximumHappinessSum2(self, happiness, k) :
        happiness.sort(reverse=True)
        total_happiness =0
        for i in range(0,k):
            current = happiness[i] -i
            if current <=0 :
                break
            total_happiness+=current
            print("CURRENT VALUE : ",current , " TOTAL_HAPPINESS : ",total_happiness)
        return total_happiness
       






obj1 = Solution1()
obj2 = Solution2()
happiness =[1,2,3]
k=2
print(obj1.maximumHappinessSum1(happiness,k))
print(obj2.maximumHappinessSum2(happiness,k))

