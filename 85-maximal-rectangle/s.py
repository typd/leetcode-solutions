class Solution(object):
    def get_max(self, hs):
        l = len(hs)
        if l == 1:
            return hs[0]
        r = 0
        stack = [-1]
        hs.append(0)
        l = len(hs)
        for i in range(l):
            h = hs[i]
            if len(stack) == 1 or h >= hs[stack[-1]]:
                stack.append(i)
                #print("append", i)
            else:
                while len(stack) >= 1 and h < hs[stack[-1]]:
                    s = stack[-1]
                    pre_s = stack[-2]
                    sh = hs[s]
                    now = sh * (i-pre_s-1)
                    if now > r:
                        r = now
                #        print(r, stack, sh, "*", pre_s+1, " to ", i-1)
                    stack.pop()
                stack.append(i)
        return r

    def maximalRectangle(self,m):
        if len(m) == 0:
            return 0
        r = 0
        last = [0] * len(m[0])
        for line in m:
            cur = [0] * len(m[0])
            for i in range(len(line)):
                if line[i] == '0':
                    cur[i] = 0
                else:
                    cur[i] = last[i] + 1
            new = self.get_max(cur)
            if new > r:
                r = new
            last = cur
        return r

def test():
    s=Solution()
    m=[ ["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]
      ]
    m=[["1"]]
    r=s.maximalRectangle(m)
    print(r)

test()
