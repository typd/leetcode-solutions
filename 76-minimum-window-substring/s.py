class Solution(object):
    def minWindow(self, s, t):
        r = ""
        win = {}
        ans = {}
        for c in t:
            win[c] = []
            if c in ans:
                ans[c] = ans[c] + 1
            else:
                ans[c] = 1
        for i in range(len(s)):
            c = s[i]
            if not (c in ans):
                continue
            target = win[c]
            target.append(i)
            if len(target) > ans[c]:
                target.remove(target[0])
            first = -1
            for c in win:
                target = win[c]
                if len(target) < ans[c]:
                    first = -1
                    break
                else:
                    if first == -1 or first > target[0]:
                        first = target[0]
            if first >= 0 and (r == "" or (i-first+1 < len(r))):
                #print("found r", first, i)
                r = s[first:(i+1)]
            #print("checking", i, c, win,r)
        return r

def test():
    s=Solution()
    ss="ADOBECODEBANC"
    t="ABC"
    ss="aaaaaaaaaaaabbbbbcdd"
    t="abcdd"
    ss="a"
    t="aa"
    ss="aa"
    t="aa"
    r=s.minWindow(ss, t)
    print(ss)
    print(t)
    print(r)

test()
