class Solution:
    def maxLength(self, str):
        
        n = len(str)

        stack = []
        max_length = 0

        for i in range(n):
            
            if str[i] == '(':
                stack.append(i)   

            else:

                stack.pop()

                if not stack:
                    stack.append(i)

                max_length = max(max_length, i - stack[-1])  

        return max_length