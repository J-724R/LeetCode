# soluiton by rock, beats 14% 
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[: 2]
        for x, y in coordinates:
            if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
                return False
        return True
    
#  faster solution by techwired8, beats 27.8%
class Solution:
    def checkStraightLine(self, coordinates):
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (x - x0) * (y1 - y0) != (y - y0) * (x1 - x0):
                return False

        return True
    
# Soltuion by rmoskalenko
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) > 2:
            A, B = coordinates[0][1] - coordinates[1][1], coordinates[1][0] - coordinates[0][0]
            C = A*coordinates[0][0] + B*coordinates[0][1]
            for point in coordinates[2:]:
                if A*point[0] + B*point[1] != C:
                    return False
        return True