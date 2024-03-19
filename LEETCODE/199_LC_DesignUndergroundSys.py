"""
Problem Link:
https://leetcode.com/problems/design-underground-system/
"""

class UndergroundSystem:
  def __init__(self):
    self.checkIns = {}
    self.checkOuts = collections.defaultdict(lambda: [0, 0])

  def checkIn(self, id, stationName, t):
    self.checkIns[id] = (stationName, t)

  def checkOut(self, id, stationName, t):
    startStation, startTime = self.checkIns.pop(id)
    route = (startStation, stationName)
    self.checkOuts[route][0] += 1
    self.checkOuts[route][1] += t - startTime

  def getAverageTime(self, startStation, endStation):
    numTrips, totalTime = self.checkOuts[(startStation, endStation)]
    return totalTime / numTrips
