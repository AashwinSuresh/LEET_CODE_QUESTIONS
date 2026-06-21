# ======================================================================
# LEETCODE 2126: PROBLEM SUMMARY & CONSTRAINTS
# ======================================================================

# THE SCENARIO:
# • You control a planet with an initial 'mass'.
# • A stream of 'asteroids' is heading toward your planet.

# THE RULES:
# • Planet Mass >= Asteroid Mass  --> Asteroid destroyed, Planet gains its mass.
# • Planet Mass < Asteroid Mass   --> Planet destroyed (Game Over).
# • Goal: Return True if ALL asteroids can be destroyed; otherwise, False.

# THE CONSTRAINTS (Why they matter for optimization):
# 1.  1 <= mass <= 10^5
#     • The planet's starting mass is small enough to fit in a standard integer.

# 2.  1 <= asteroids.length <= 10^5
#     • There can be up to 100,000 asteroids. An O(N^2) solution will 
#       Time Out (TLE). We need an O(N log N) or O(N) solution.

# 3.  1 <= asteroids[i] <= 10^5
#     • The maximum size of any asteroid is capped at 100,000. 
#     • This specific cap is what allows us to use the super-fast 
#       Bucket/Counting Sort approach instead of standard sorting!
# ======================================================================


from typing import List

#space complexity optimized approach
class Solution1:
    def asteroidsDestroyed1(self, mass: int, asteroids: List[int]) -> bool:
        n=len(asteroids)
        asteroids.sort()
        # print(asteroids)
        for asteroid in asteroids:
            # print(f"current mass : {mass:<10}|current asteroid : {asteroid:<10}")
            if mass<asteroid:
                return False
            mass+=asteroid
        return True


#time complexity optimized approach
class Solution2:
    def asteroidsDestroyed2(self, mass: int, asteroids: List[int]) -> bool:
        bucket_size = 1000      
        # each bucket will have 1000 values stored , and there are 100 such buckets, so it can store 1000*100 = 10^5 values , constraint asteroid.length <= 10^5 
        buckets = [[] for _ in range(101)]
        for ast in asteroids:
            buckets[ast//bucket_size].append(ast)

# ======================================================================
# MINI-EXAMPLE: BUCKET SORT WITH SIZE 10
# ======================================================================

# Setup: 
# • BUCKET_SIZE = 10
# • Asteroids to sort: [35, 12, 7, 19]
# • Formula used: bucket_index = mass // 10

# Step-by-Step Distribution:

# 1. Asteroid 35:
#    • 35 // 10 = Index 3  -> Moves to Bucket 3
#    • Current Buckets: [[], [], [], [35]]

# 2. Asteroid 12:
#    • 12 // 10 = Index 1  -> Moves to Bucket 1
#    • Current Buckets: [[], [12], [], [35]]

# 3. Asteroid 7:
#    • 7 // 10 = Index 0   -> Moves to Bucket 0
#    • Current Buckets: [[7], [12], [], [35]]

# 4. Asteroid 19:
#    • 19 // 10 = Index 1  -> Moves to Bucket 1
#    • Final Buckets:   [[7], [12, 19], [], [35]]

        for bucket in buckets:
            if not bucket:
                continue
            bucket.sort()
            for ast in bucket:
                if ast>mass:
                    return False
                mass+=ast

                if mass>=100000:
                    return True
        return True
    








# ======================================================================
# TEST RUN RUNNER FOR SOLUTION 1 AND SOLUTION 2
# ======================================================================

def run_tests():
    sol1 = Solution1()
    sol2 = Solution2()

    test_cases = [
        {
            "name": "Standard Survivable Case (Your failing image case fixed by bucket sort order)",
            "mass": 14359,
            "asteroids": [77244, 19898, 13062, 79891, 33924, 90485, 2244],
            "expected": True
        },
        {
            "name": "Immediate Failure (First asteroid is too large)",
            "mass": 5,
            "asteroids": [10, 1, 2, 3],
            "expected": False
        },
        {
            "name": "Exact Boundary Match (Mass equals asteroid size)",
            "mass": 10,
            "asteroids": [10, 20, 40],
            "expected": True  # 10->20->40->80
        },
        {
            "name": "Trigger Early Exit Optimization (Mass rapidly explodes past 10^5)",
            "mass": 50000,
            "asteroids": [60000, 1000, 2000, 99999],
            "expected": True  # Becomes 50k + 1k + 2k = 53k, can handle everything
        },
        {
            "name": "All Same Value Asteroids",
            "mass": 10,
            "asteroids": [10, 10, 10, 10],
            "expected": True
        }
    ]

    print(f"{'TEST CASE NAME':<70} | {'SOL 1 RESULT':<12} | {'SOL 2 RESULT':<12} | {'EXPECTED'}")
    print("-" * 115)
    
    for i, tc in enumerate(test_cases, 1):
        # We pass a copy of the list because Solution1 modifies it in-place via .sort()
        res1 = sol1.asteroidsDestroyed1(tc["mass"], list(tc["asteroids"]))
        res2 = sol2.asteroidsDestroyed2(tc["mass"], list(tc["asteroids"]))
        
        status1 = "PASS ✅" if res1 == tc["expected"] else "FAIL ❌"
        status2 = "PASS ✅" if res2 == tc["expected"] else "FAIL ❌"
        
        print(f"TC {i}: {tc['name']:<64} | {status1:<12} | {status2:<12} | {tc['expected']}")

# Execute the runner
run_tests()