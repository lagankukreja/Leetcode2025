class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = ''
        open_count = 0
        for char in s:
            if char.isalpha():
                res += char
    
            if char == '(':
                open_count += 1
                res += char
            if char == ')':
                if open_count == 0:
                    continue
                else:
                    open_count -= 1
                    res += char
        if open_count > 0:
            for i in range(len(res)-1, -1, -1):
                if open_count == 0:
                    break
                if res[i] == '(':
                    open_count -= 1
                    res = res[:i] + res[i+1:]
        return res