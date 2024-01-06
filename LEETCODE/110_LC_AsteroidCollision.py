"""
Problem Link:
https://leetcode.com/problems/asteroid-collision/
"""

class Solution:
    def asteroidCollision(self, asteroids):
        strike = []
        for asteroid in asteroids:
            if not strike or asteroid > 0:
                strike.append(asteroid)
            else:
                while strike and strike[-1] > 0 and strike[-1] < abs(asteroid):
                    strike.pop()
                if strike and strike[-1] == abs(asteroid):
                    strike.pop()
                else:
                    if not strike or strike[-1] < 0:
                        strike.append(asteroid)
        return strike
