class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:

        points.sort(key = lambda x: x[1])     
        t, b = 1, points[0][1]
        for start, end in points:
            if b < start:                   
                b = end                   
                t += 1                      
        return t
