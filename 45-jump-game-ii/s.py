class Solution(object):
    def jump(self, nums):
        steps=[len(nums) + 1] * len(nums)
        steps[0]=0
        farest = 0
        for i in range(len(nums)):
            js = list(range(max(farest-i, 0), nums[i]))
            for j in js:
                if i+j+1 < len(nums):
                    steps[i+j+1] = min(steps[i+j+1], steps[i]+1)
                    farest = max(farest, i+j)
        return steps[-1]

def test():
    s=Solution()
    a=[1,1,1,1,1]
    a=[2,3,1,1,4]
    a=[1,1,1,1]
    r=s.jump(a)
    print(a)
    print(r)

test()
