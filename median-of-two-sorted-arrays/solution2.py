class Solution(object):
    # rewrote from https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-shu-b/
    def findMedianSortedArrays(self, A, B):
        size_A = len(A)
        size_B = len(B)
        if size_A > size_B:
            size_A, size_B, A, B = size_B, size_A, B, A
        half_size = int((size_A + size_B + 1) / 2)
        imin = 0
        imax = size_A
        print(A)
        print(B)
        i = 0
        j = 0
        while imin < imax:
            i = int((imin + imax) / 2)
            j = half_size - i
            print("i range:", imin, imax, ", i:", i, "j:", j)
            if i>0 and j<size_B and A[i-1] > B[j]:
                imax = i - 1
            elif i<size_A and A[i]<B[j-1]:
                imin=i + 1
            else: # found i
                break
        i = int((imin + imax) / 2)
        j = half_size - i
        print("i range:", imin, imax, ", i:", i, "j:", j)
        if i == 0:
            max_left = B[j-1]
        elif j == 0:
            max_left = A[i-1]
        else:
            max_left = max(A[i-1], B[j-1])
        if (size_A + size_B)%2 == 1:
            return max_left

        if i == size_A:
            min_right = B[j]
        elif j == size_B:
            min_right = A[i]
        else:
            min_right = min(A[i], B[j])
        return (float(max_left) + min_right)/2

def test():
    s = Solution()
    a1 = [1,1,1,1,1]
    a2 = [2,2,2,2]
    a1 = [2,2,2,3,3,3,4,4]
    a2 = [0,0,1,1,1,1,9,9,9,9]
    a1 = [1,2,3,3,4]
    a2 = [1,2,4]
    a1 = [1,3]
    a2 = [2]
    a1 = []
    a2 = [1]
    a1 = [2]
    a2 = []
    r = s.findMedianSortedArrays(a1,a2)
    print(a1)
    print(a2)
    print(r)

test()


