class Solution(object):
    def permute(self, nums): 
        result = []          
        
        def backtrack(path, remaining):
            if not remaining:
                result.append(path[:])
                return
            for i in range(len(remaining)):
                next_path = path + [remaining[i]]
                next_rem = remaining[:i] + remaining[i+1:]
                backtrack(next_path, next_rem)
                
        backtrack([], nums)
        return result


sol = Solution()               
print(sol.permute([1, 2, 3]))  