class Solution(object):
    def findSubstring(self,s,words):
        r = []
        wc = len(words)
        if wc == 0:
            return r
        wl = len(words[0])
        sl = len(s)
        m = {}
        for w in words:
            if not w in m:
                m[w] = 1
            else:
                m[w] = m[w]+1
        i = 0
        print(m)
        while i + wc * wl <= sl:
            #print("checking", s[i:])
            count_down = m.copy()
            for j in range(wc):
                w = s[i+j*wl:i+j*wl+wl]
                if not w in count_down:
                    break
                else:
                    count_down[w] = count_down[w] - 1
            #print("  ", count_down)
            all_right = True
            for k in count_down:
                if count_down[k] != 0:
                    all_right = False
                    break
            if all_right:
                r.append(i)
            i+=1
        return r

def test():
    ss = Solution()
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    s = "wordgoodgoodgoodbestword",
    words = ["word","good","best","word"]
    s= "wordgoodgoodgoodbestword"
    words=["word","good","best","good"]
    r = ss.findSubstring(s,words)
    print(s)
    print(words)
    print(r)

test()


