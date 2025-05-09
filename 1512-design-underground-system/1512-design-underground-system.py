class UndergroundSystem:

    def __init__(self):
        self.stationCheckins = defaultdict(tuple)
        self.stationAverageTimes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.stationCheckins[id]=(t,stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        stations = (self.stationCheckins[id][1],stationName)
        entrytime = self.stationCheckins[id][0]
        if stations in self.stationAverageTimes:
            self.stationAverageTimes[stations][0]+= (t-entrytime)
            self.stationAverageTimes[stations][1] += 1
        else:
            self.stationAverageTimes[stations] = [t-entrytime, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime = self.stationAverageTimes[(startStation,endStation)][0]
        num = self.stationAverageTimes[(startStation,endStation)][1]
        return totalTime / num


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)