# Solution by techwired8
class SnapshotArray:
    def __init__(self, length: int):
        self.array = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.array[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        history = self.array[index]
        left, right = 0, len(history) - 1

        while left <= right:
            mid = (left + right) // 2
            if history[mid][0] <= snap_id:
                left = mid + 1
            else:
                right = mid - 1

        return history[right][1]
    

# Faster solution by idontknoooo, beats 77%
class SnapshotArray:
    def __init__(self, length: int):
        self.cache = collections.defaultdict(lambda : collections.OrderedDict())
        self.i = 0

    def set(self, index: int, val: int) -> None:
        self.cache[index][self.i] = val

    def snap(self) -> int:
        self.i += 1
        return self.i-1
        
    @lru_cache(maxsize=None)    
    def get(self, index: int, snap_id: int) -> int:
        if index not in self.cache: return 0
        else:
            idx_cache = self.cache[index]
            if snap_id in idx_cache: return idx_cache[snap_id]
            else:
                keys = list(idx_cache.keys()) 
                i = bisect.bisect(keys, snap_id)
                if snap_id > keys[-1]: return idx_cache[keys[-1]]
                elif i == 0: return 0
                else: return idx_cache[keys[i-1]]