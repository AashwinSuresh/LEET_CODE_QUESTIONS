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

# ================================================

# SEGMENT TREE + OBSTACLE PROBLEM RECALL NOTES

# ================================================

# -------------------------

# SEGMENT TREE BASICS

# -------------------------

# A Segment Tree is a binary tree used to store summary information

# about ranges (segments) of an array.

# In this problem, every node stores the MAXIMUM value in its range.

# Example:

#

# Array:

# [2,5,1,8,4,6,3,9]

#

# Tree:

#

# [0,7]=9

# /            \

# [0,3]=8          [4,7]=9

# /      \         /      \

# [0,1]=5  [2,3]=8  [4,5]=6  [6,7]=9

# IMPORTANT:

# The interval [l,r] written on a node tells us WHICH INDICES

# the node covers, NOT what value should be stored there.

# The stored value is simply:

#

# maximum among the indices covered by that node.

# -------------------------

# TREE ARRAY REPRESENTATION

# -------------------------

# node 1 -> root

#

# left child  = 2*node

# right child = 2*node+1

# Maximum size needed = 4*N

# tree = [0]*(4*N)

# -------------------------

# UPDATE FUNCTION

# -------------------------

# update(node,start,end,idx,val)

# start,end

# Range covered by the current node.

# idx

# Which array index we want to modify.

# val

# New value to store at idx.

# Example:

#

# update(1,0,7,2,10)

#

# means:

#

# arr[2]=10

# Process:

#

# Root -> Leaf

#

# Reach [2,2]

#

# Store value 10

#

# While returning,

# every parent recalculates:

#

# tree[node]=max(left_child,right_child)

# Thus update propagates:

#

# Root -> Leaf -> Root

# -------------------------

# QUERY FUNCTION

# -------------------------

# query(node,start,end,l,r)

# Returns the maximum value inside [l,r].

# Three cases:

# 1) NO OVERLAP

#

# Current node completely outside query range.

#

# return 0

# Condition:

#

# if r<start or end<l

# In THIS problem l=0 always,

# so effectively only

#

# if r<start

#

# matters.

# 2) COMPLETE OVERLAP

#

# Current node lies completely inside query range.

#

# Return tree[node]

#

# No need to go deeper.

# 3) PARTIAL OVERLAP

#

# Ask both children and combine answers.

#

# p1=query(left child)

# p2=query(right child)

#

# return max(p1,p2)

# Query movement:

#

# Root -> Some branches -> Root

# =====================================================

# OBSTACLE PROBLEM

# =====================================================

# obstacles list stores obstacle coordinates in sorted order.

# Example:

#

# obstacles=[0,4,7]

# -------------------------

# GAP ARRAY CONCEPT

# -------------------------

# The segment tree DOES NOT store coordinates.

# It stores gap lengths.

# Specifically:

#

# gap_array[i]

#

# = length of the gap whose RIGHT ENDPOINT is i.

# Example:

#

# 0 ----- 4 ---- 7

#

# Gap lengths:

#

# 0→4 length 4

# 4→7 length 3

# Therefore:

# gap_array[4]=4

# gap_array[7]=3

# All other entries are 0.

# Example:

#

# gap_array=[0,0,0,0,4,0,0,3]

# -------------------------

# MEANING OF SEGMENT TREE NODES

# -------------------------

# Node [6,7]

#

# means:

#

# "Among gaps ending at coordinates 6 and 7,

# what is the largest gap length?"

# Therefore:

#

# max(gap_array[6],gap_array[7])

# Node [4,7]

#

# means:

#

# "Among gaps ending between coordinates 4 and 7,

# what is the largest gap length?"

# It DOES NOT mean

#

# "Gap from coordinate 4 to coordinate 7"

# =====================================================

# INSERTING AN OBSTACLE (q[0]==1)

# =====================================================

# Find:

#

# previous obstacle

# next obstacle

# Example:

#

# Before:

#

# 0 ---------- 10

#

# Insert obstacle at 6

#

# After:

#

# 0 ---- 6 ---- 10

# Old gap:

#

# length 10 ending at 10

# New gaps:

#

# length 6 ending at 6

# length 4 ending at 10

# Therefore:

# update(idx=6,val=6)

# update(idx=10,val=4)

# Remember:

#

# idx = right endpoint

#

# val = gap length

# =====================================================

# TYPE-2 QUERY

# =====================================================

# q=[2,lim,sz]

# Means:

#

# "Is there a continuous free segment of length sz

# somewhere before coordinate lim?"

# -----------------------------------------------------

# max_gap

# -----------------------------------------------------

# max_gap=query(0,lim)

# Meaning:

#

# Largest COMPLETE gap whose right endpoint <= lim

# -----------------------------------------------------

# Problem with max_gap

# -----------------------------------------------------

# Example:

#

# 0 ---- 4 -------------------- 12

#

# lim=9

# Segment tree only knows:

# 0→4 length 4

# 4→12 length 8

# Since endpoint 12 > 9,

# gap 4→12 is invisible.

# Thus:

# max_gap=4

# But geometrically:

# 4 ----- 9

# length = 5

# We would miss this.

# -----------------------------------------------------

# trailing_gap

# -----------------------------------------------------

# Find previous obstacle before lim.

# Example:

#

# obstacles=[0,4,12]

#

# lim=9

# previous obstacle=4

# Therefore:

# trailing_gap=9-4=5

# Meaning:

#

# Size of the unfinished gap containing lim.

# -----------------------------------------------------

# Final Answer

# -----------------------------------------------------

# answer=max(max_gap,trailing_gap)

# Because the largest usable gap before lim is either:

# 1) A complete gap already stored in the segment tree.

# OR

# 2) The unfinished gap containing lim.

# No third possibility exists.

# =====================================================

# BIGGEST TAKEAWAY

# =====================================================

# Segment Tree knows ONLY complete gaps.

# trailing_gap handles the partial gap containing lim.

# Together they guarantee that we never miss

# the largest available space.


