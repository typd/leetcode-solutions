class Solution(object):
    def can_be_zero(self,p):
        for i in range(len(p)):
            if p[i] != "*":
                return False
        return True

    def trim(self,p):
        while "**" in p:
            p = p.replace("**", "*")
        return p

    def isMatch(self, s, p):
        self.dp = {}
        new_p = self.trim(p)
        print(new_p)
        return self.check(s, new_p)

    def check(self, s, p):
        dp = self.dp
        if (s, p) in dp:
            return dp[(s, p)]

        if len(s)==0:
            if len(p)==0:
                return True
            if self.can_be_zero(p):
                return True
            return False
        if len(p)==0:
            return False
        if p[0] == '?':
            dp[(s,p)] = self.check(s[1:],p[1:])
            return dp[(s,p)]
        if p[0] == "*":
            if self.check(s[1:],p):
                dp[(s,p)] = True
                return True
            if self.check(s,p[1:]):
                dp[(s,p)] = True
                return True
            dp[(s,p)] = False
            return False
        if p[0] == s[0]:
            dp[(s,p)] = self.check(s[1:],p[1:])
            return dp[(s,p)]
        else:
            return False

def test():
    ss = Solution()
    s = "aaa"
    p = "abb"
    s = "bbb"
    p = "bbb"
    s = "ccccccc"
    p = "c*"
    s = "ccccccc"
    p = "a*c*"
    s = "abcd"
    p = ".*"
    s = "bbbba"
    p = ".*a*a"
    s="aab"
    p="a*ab"
    s="aaaaaaaaaaaaab"
    p="a*a*a*a*a*a*a*a*b"
    s = "bbb"
    p = "b?b"
    s="aaabababaaabaababbbaaaabbbbbbabbbbabbbabbaabbababab"
    p="*ab***ba**b*b*aaab*b"
    s="abbaabbbbababaababababbabbbaaaabbbbaaabbbabaabbbbbabbbbabbabbaaabaaaabbbbbbaaabbabbbbababbbaaabbabbabb"
    p="***b**a*a*b***b*a*b*bbb**baa*bba**b**bb***b*a*aab*a**"
    r = ss.isMatch(s,p)
    print("s:", s)
    print("p:", p)
    print(r)

test()


