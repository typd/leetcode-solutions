class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def valid(size1, size2, p1, p2):
            if p1 < 1 or p1 > size1:
                return False
            if p2 < 1 or p2 > size2:
                return False
            return True

        size1 = len(nums1)
        size2 = len(nums2)

        p1 = int((size1 + 1) / 2)
        p2 = int((size2 + 1) / 2)
        if (p1 * 2 == size1) and (p2 * 2 == size2):
            if p1 < size1:
                p1 += 1
            elif p2 < size2:
                p2 += 1
            else:
                # both length == 1
                return (0.0 + nums1[0] + nums2[0]) / 2
        print(size1, size2)
        print(p1, p2)

        diff = abs(nums1[p1 - 1] - nums2[p2 - 1])
        done = False
        while not done:
            print("nums1[{}]: {}".format(p1, nums1[p1-1]), ";", "nums2[{}]: {}".format(p2, nums2[p2-1]))
            if (nums1[p1 - 1] == nums2[p2 - 1]):
                done = True
                break
            else:
                if (nums1[p1 - 1] > nums2[p2 - 1]):
                    new_p1 = p1 - 1
                    new_p2 = p2 + 1
                elif (nums1[p1 - 1] < nums2[p2 - 1]):
                    new_p1 = p1 + 1
                    new_p2 = p2 - 1
                if not valid(size1, size2, new_p1, new_p2):
                    done = True
                    break
                new_diff = abs(nums1[new_p1 - 1] - nums2[new_p2 - 1])
                if new_diff <= diff:
                    p1 = new_p1
                    p2 = new_p2
                    diff = new_diff
                else:
                    done = True
                    break
        print("nums1[{}]: {}".format(p1, nums1[p1-1]), ";", "nums2[{}]: {}".format(p2, nums2[p2-1]))

        if (size1 + size2) % 2 == 1:
            n1 = 0
            n2 = 0
            if p1 == 1:
                
            return float(max(nums1[p1 - 1], nums2[p2 - 1]))
        else:
            if nums1[p1-1] == nums2[p2-1]:
                return float(nums1[p1-1])
            bigger = 0
            smaller = 0
            if nums1[p1-1] > nums2[p2-1]:
                bigger = nums1[p1-1]
                if p1>1:
                    smaller = max(nums1[p1-2], nums2[p2-1])
                else:
                    smaller = nums2[p2-1]
            elif nums1[p1-1] < nums2[p2-1]:
                bigger = nums2[p2-1]
                if p2 > 1:
                    smaller = max(nums2[p2-2], nums1[p1-1])
                else:
                    smaller = nums1[p1-1]
            return float(bigger + smaller) / 2

def test():
    s = Solution()
    a1 = [1,2,3,3,4]
    a2 = [1,2,4]
    a1 = [2,2,2,3,3,3,4,4]
    a2 = [0,0,1,1,1,1,9,9,9,9]
    a1 = [1,1,1,1,1]
    a2 = [2,2,2,2]
    r = s.findMedianSortedArrays(a1,a2)
    print(a1)
    print(a2)
    print(r)

test()


