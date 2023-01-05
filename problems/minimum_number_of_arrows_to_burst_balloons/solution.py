class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x : x[0], reverse=True)
        n=len(points)
        balloon=points[0]
        arrow=1
        for i in range(1, n):
            newBalloon=points[i]
            if balloon[0]<=newBalloon[-1]:
                continue
            else:
                arrow+=1
                balloon=newBalloon
        return arrow
