# reference :  https://leetcode.com/problems/find-median-from-data-stream/discuss/

from heapq import *
from decimal import Decimal, ROUND_HALF_UP

class runningMedian:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return Decimal(float(large[0])).quantize(0, ROUND_HALF_UP)
        return Decimal((large[0] - small[0]) / 2.0).quantize(0, ROUND_HALF_UP)
