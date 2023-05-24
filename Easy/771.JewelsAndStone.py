
# My solution
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count, j = 0, {} 
        for i in jewels:
            j[i] =  1

        for s in stones:
            if s in j: 
                count += 1

        return count
    
# One of the fastest solutions found
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewel = set(J)
        return sum( 1 for item in S if item in jewel )
    

    # aproach similar to higher level langauges
    def numJewelsInStonesII(self, J: str, S: str) -> int:
        count_of_jewels = 0

        for j in J:
            count_of_jewels += S.count(j)

        return count_of_jewels