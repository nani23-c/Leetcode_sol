class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def square(point):
            return point[0]*point[0]+point[1]*point[1]
        points.sort(key=square)
        return points[:k]

        