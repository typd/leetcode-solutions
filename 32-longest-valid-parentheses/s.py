class Solution(object):
    def longestValidParentheses(self, s):
        print(s)
        stack = [-1]
        r=0
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            elif s[i]==")":
                if len(stack)==1:
                    stack=[i]
                else:
                    index = stack.pop()
                    index = stack[-1]
                    r = max(r, i-index)
            print(s[i], stack)
        return r

def test():
    ss = Solution()
    s=")(()())("
    s=")()()("
    r = ss.longestValidParentheses(s)
    print(r)

test()
