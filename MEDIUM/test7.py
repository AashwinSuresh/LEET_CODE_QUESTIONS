

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        n=len(asteroids)
        asteroids.sort()
        # print(asteroids)
        for asteroid in asteroids:
            # print(f"current mass : {mass:<10}|current asteroid : {asteroid:<10}")
            if mass<asteroid:
                return False
            mass+=asteroid
        return True
