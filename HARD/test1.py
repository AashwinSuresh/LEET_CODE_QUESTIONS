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
                


#OPTIMIZED APPROACH : 


import bisect

class SegTree:
    def __init__(self,size):
        self.tree = [0]*4*size
    def update(self,node,start,end,idx,val):
        #idx : shows gap ending at ..
        if (start==end):
            self.tree[node] = val
            return
        mid = (start+end)//2
        if idx<=mid:
            self.update(2*node,start,mid,idx,val)
        else:
            self.update(2*node+1,mid+1,end,idx,val)
        
        self.tree[node]=max(self.tree[2*node],self.tree[2*node+1])

    def query(self,node,start,end,l,r):
        if r<start:
            return 0
        elif l<=start and end<=r:
            return self.tree[node]
        mid = (start+end)//2
        p1 = self.query(2*node,start,mid,l,r)
        p2 = self.query(2*node+1,mid+1,end,l,r)
        return max(p1,p2)

class Solution:
    def getResults(self, queries: List[List[int]]):
        
        max_coord = max(q[1] for q in queries)+1
        print(f"the max coord is : {max_coord}")
        st = SegTree(max_coord)
        obstacles = [0,max_coord]
        st.update(1,0,max_coord,max_coord,max_coord)
        ans = []
        for q in queries :
            if q[0] == 1:
                i = bisect.bisect_left(obstacles,q[1])
                prev_block = obstacles[i-1]
                next_block = obstacles[i]
                obstacles.insert(i,q[1])

                st.update(1,0,max_coord,q[1],q[1]-prev_block)
                st.update(1,0,max_coord,next_block,next_block-q[1])

            elif q[0] ==2:
                completed_max_gap = st.query(1,0,max_coord,0,q[1])
                
                #to find trailing gap:
                i = bisect.bisect_left(obstacles,q[1])
                prev_block = obstacles[i-1]
                trailing_gap = q[1]-prev_block

                print(f"completed max gap : {completed_max_gap} trailing gap : {trailing_gap}")

                if max(completed_max_gap,trailing_gap)>=q[2]:
                    ans.append(True)
                else:
                    ans.append(False)

        #     #FOR PRINTNG THE TREE : 
        # for i in range(1,len(st.tree)):
        #     print(f"node{i}  : {st.tree[i]}")

        return ans
                
#time to push
    