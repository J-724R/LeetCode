class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")
            

# With dictionarry, its not as fast but is more scalable
class Solution:
    def interpret(self, s: str) -> str:
        d = {"(al)":"al", "()":"o","G":"G"}
        tmp= ""
        res=""
        for i in range(len(s)):
            tmp+=s[i]
            if(tmp in d):
                res+=d[tmp]
                tmp=""
        return res