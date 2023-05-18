# intuition

# crate hashtable with all the char and set them to 0
# use two pointers one for string and one for counter
# loop trough string 
#     check frequency, if char is in substring reset to "" 
#     add char to subtring 
# return substring and len(subtring)


# list solution is more eficient than set

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = maxCount = 0
        seen = []

        for x in s:
            if x not in seen:
                seen.append(x)
                count=len(seen)
                if count > maxCount:
                    maxCount = count
            else:
                seen[:seen.index(x)+1] = []
                seen.append(x)
                count = 0
        return maxCount  
    
class Solution:
    def lengthOfLongestSubstring(self, s):
        window = set()
        beg, end, ans, n = 0, 0, 0, len(s)
        
        while beg < n and end < n:
            if s[end] not in window:
                if end + 1 < n: window.add(s[end])
                end += 1
                ans = max(ans, end - beg)
            else:
                window.remove(s[beg])
                beg += 1
                
        return ans