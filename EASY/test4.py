# # 3633. Earliest Finish Time for Land and Water Rides I

# ## Problem Description
# You are given two categories of theme park attractions: land rides and water rides.

# ### Land rides
# * `landStartTime[i]` – the earliest time the ith land ride can be boarded.
# * `landDuration[i]` – how long the ith land ride lasts.

# ### Water rides
# * `waterStartTime[j]` – the earliest time the jth water ride can be boarded.
# * `waterDuration[j]` – how long the jth water ride lasts.

# A tourist must experience exactly one ride from each category, in either order.
# A ride may be started at its opening time or any later moment.
# If a ride is started at time `t`, it finishes at time `t + duration`.

# Immediately after finishing one ride the tourist may board the other (if it is already open) or wait until it opens.

# Return the earliest possible time at which the tourist can finish both rides.

# ## Constraints & Rules
# * Exactly one land ride and exactly one water ride must be taken.
# * The rides can be taken in any order: (Land ➔ Water) OR (Water ➔ Land).
# * If transitioning to the next ride before its start time, the tourist must wait until the ride opens.

# ## Complexity Requirements
# * **Time Complexity:** O(N + M) 
# * **Space Complexity:** O(1)


from typing import List




class Solution  :
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        l_min = min(start+dur for start,dur in zip(landStartTime,landDuration))
        w_min = min(start+dur for start,dur in zip(waterStartTime,waterDuration))
        


        land_then_water = min(max(l_min,start)+dur for start,dur in zip(waterStartTime,waterDuration))
        water_then_land = min(max(w_min,start)+dur for start,dur in zip(landStartTime,landDuration))


        return min(land_then_water,water_then_land)
    

if __name__ == "__main__":
    # 1. Define the input lists (Using Example 1 from earlier)
    land_start = [1, 3, 5]
    land_dur = [2, 2, 4]
    water_start = [2, 4, 1]
    water_dur = [3, 1, 5]

    # 2. Instantiate the class object
    solver = Solution()

    # 3. Call the function by passing the arguments
    result = solver.earliestFinishTime(land_start, land_dur, water_start, water_dur)

    # 4. Print the returned value
    print(f"The earliest possible finish time is: {result}")

        



