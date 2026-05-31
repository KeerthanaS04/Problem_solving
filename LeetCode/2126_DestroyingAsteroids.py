from typing import List
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        for asteroid_mass in asteroids:
            if mass<asteroid_mass:
                return False
            mass+=asteroid_mass
        return True