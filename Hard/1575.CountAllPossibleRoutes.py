# Solution by brianchiang_tw
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        cost = lambda i, j: abs( locations[i] - locations[j] )
        @lru_cache(None)
        def dfs(cur, remain_fuel):
            if remain_fuel < 0:
                return 0
            
            return sum( dfs(next_city, remain_fuel - cost(cur, next_city) )for next_city in range(len(locations) ) if cur != next_city ) + ( cur == finish )

        constant = ( 10 ** 9 + 7 )
        return dfs(cur=start, remain_fuel=fuel) % constant