# Problem: Seat Reservation Manager - https://leetcode.com/problems/seat-reservation-manager/description/

class SeatManager:

    def __init__(self, n: int):
        self.unres = []
        for i in range(1,n+1):
            self.unres.append(i)
    def reserve(self) -> int:
        return heapq.heappop(self.unres)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.unres,seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)