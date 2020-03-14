class Solution(object):
    def firstMissingPositive(self, nums):
        size = len(nums)
        for i in range(size):
            v = nums[i]
            if v<1 or v > size:
                nums[i]=size+10
        for i in range(size):
            v = abs(nums[i])
            if v >0 and v<=size and nums[v-1]>0:
                nums[v-1] = -nums[v-1]
        for i in range(size):
            if nums[i] >=0:
                return i+1
        return size + 1

def test():
    s = Solution()
    a=[1,2,7,8,3,9,11,12]
    a=[1,2,3]
    a=[1,2,3,0]
    a=[1,1]
    a=[1,2,0]
    a=[0,1,2]
    a=[1]
    print(a)
    r = s.firstMissingPositive(a)
    print(a)
    print(r)


test()
