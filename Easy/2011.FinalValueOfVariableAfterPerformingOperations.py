class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        if operations == None: return 0
        for op in operations:
            if op == "--X" or op == "X--":
                x -= 1
            if op == "++X" or op == "X++":
                x += 1
        return x
    

# with built in count()
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        A=operations.count("++X") 
        B=operations.count("X++")
        
        return A+B-(len(operations)-A-B)