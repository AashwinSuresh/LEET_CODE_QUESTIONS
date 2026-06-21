# # Problem Statement: Minimum Cost of Buying Candies With Discount

# A shop is selling candies at a special discount. For every two candies purchased, the shop gives you a third candy for free.

# The cost of each candy is given as an array of integers `cost` where `cost[i]` is the cost of the i-th candy.

# The candy given for free must have a cost that is less than or equal to the minimum cost of both the purchased candies.
# - For example, if you buy candies with costs 2 and 3, you can take a candy with a cost of 2, 1, or any lower value for free. However, you cannot take a candy with a cost of 4 for free.

# Given the `cost` array, return the minimum cost of buying all the candies.

# ## Constraints:
# - 1 <= cost.length <= 100
# - 1 <= cost[i] <= 100

# ## Examples:

# ### Example 1:
# Input: cost = [3,3,3,1]
# Output: 7
# Explanation: 
# - Buy the two candies with cost 3 and 3.
# - You take the third candy with cost 3 for free.
# - Finally, you buy the remaining candy with cost 1.
# Total cost = 3 + 3 + 1 = 7.

# ### Example 2:
# Input: cost = [6,5,7,9,2,2]
# Output: 23
# Explanation: 
# - The candies are bought in this order: buy 9 and 7, get 6 free.
# - Buy 5 and 2, get 2 free.
# Total cost = 9 + 7 + 5 + 2 = 23.

# ### Example 3:
# Input: cost = [5,5]
# Output: 10
# Explanation: 
# - There are only 2 candies, so you buy both of them. No free candy can be taken.
# Total cost = 5 + 5 = 10.




from typing import List


class Solution1:
    def minimumCost1(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        idx = 0
        min_cost=0
        while cost:
            candy_1 = cost.pop(0)
            if not cost:
                return min_cost+candy_1
            candy_2 = cost.pop(0)
            min_cost+=candy_1+candy_2
            if not cost:
                return min_cost
            free_candy = cost.pop(0)
        return min_cost

#optimized approach 
class Solution2:
    def minimumCost2(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        del cost[2:len(cost):3]     #delete every third element (which is the free one)
        return sum(cost)
    



# --- TEST RUNNER SCRIPTH ---
if __name__ == "__main__":
    s1 = Solution1()
    s2 = Solution2()

    # List of test cases: (input_data, expected_output, description)
    test_cases = [
        (
            [3, 3, 3, 1], 
            7, 
            "Example 1: Buy 3 and 3, get 3 free. Buy 1, total = 3 + 3 + 1"
        ),
        (
            [6, 5, 7, 9, 2, 2], 
            23, 
            "Example 2: Buy 9 and 7 (6 free), Buy 5 and 2 (2 free), total = 9 + 7 + 5 + 2"
        ),
        (
            [5, 5], 
            10, 
            "Edge Case: Only 2 items (no free candy available)"
        ),
        (
            [10], 
            10, 
            "Edge Case: Only 1 item"
        ),
        (
            [1, 2, 3], 
            5, 
            "Standard Group of 3: Buy 3 and 2, get 1 free"
        ),
        (
            [10, 20, 30, 40, 50, 60, 70, 80, 90], 
            330, 
            "Large sorted groups: Drops 70, 40, and 10"
        )
    ]

    print("=" * 60)
    print(f"{'Test Case Description':<50} | {'S1 Result':<10} | {'S2 Result':<10} | {'Expected':<10}")
    print("=" * 60)

    for cost_array, expected, desc in test_cases:
        # We pass a copy of the list because your methods modify the list in-place
        res1 = s1.minimumCost1(cost_array.copy())
        res2 = s2.minimumCost2(cost_array.copy())
        
        status1 = "✅" if res1 == expected else "❌"
        status2 = "✅" if res2 == expected else "❌"
        
        print(f"{desc[:48]:<50} | {f'{res1} {status1}':<10} | {f'{res2} {status2}':<10} | {expected:<10}")