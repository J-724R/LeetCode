# Solution by Obose, beats 81.47%
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        keys = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '@':
                    start = (i, j)
                elif grid[i][j].islower():
                    keys += 1
        q = collections.deque()
        q.append((start[0], start[1], 0))
        visited = set()
        visited.add((start[0], start[1], 0))
        steps = 0
        while q:
            for _ in range(len(q)):
                row, col, key = q.popleft()
                if grid[row][col].islower():
                    key |= 1 << (ord(grid[row][col]) - ord('a'))
                if key == (1 << keys) - 1:
                    return steps
                for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] != '#':
                        if grid[r][c].isupper() and key & (1 << (ord(grid[r][c]) - ord('A'))) == 0:
                            continue
                        if (r, c, key) not in visited:
                            q.append((r, c, key))
                            visited.add((r, c, key))
            steps += 1
        return -1