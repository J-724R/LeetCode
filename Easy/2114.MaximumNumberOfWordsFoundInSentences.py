class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max = 0
        for s in sentences:
            if s.count(" ") > max:
                max = s.count(" ")
        return max + 1