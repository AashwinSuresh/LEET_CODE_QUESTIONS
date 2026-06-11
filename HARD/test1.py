class Solution1:
    def getResults1(self, queries: list[list[int]]):
        blocks=[]
        ans =[]
        for i in range(len(queries)):
            q = queries[i]
            print(f"\ncurrently processing : {q}")
            if q[0] == 1:
                print("type 1")
                blocks.append(q[1])
                blocks.sort()
                print(f"current blocks : {blocks}")
            elif q[0] ==2:
                print("type 2")
                lim = q[1]
                sz = q[2]
                for l in range(lim-sz+1):
                    u = l+sz
                    print(f"lower limit : {l} upper limit : {u}")
                    intersects = False
                    for  block in blocks:
                        print(f"current block : {block}")
                        if l < block < u:
                            print(f"intersection happens with block : {block}")
                            intersects =True
                            break
                    if not intersects :
                        print("Intersection wont happen , ans updated with True")
                        ans.append(True)
                        break
                else :
                    print("Not possible without intersection , ans updated with False   ")
                    ans.append(False)
                
        return ans
                
        