class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        nums1 = float('inf')
        nums2 = float('inf')

        for element in nums:
            nums3 = element

            if nums3 <= nums1:
                nums1 = nums3
            elif nums3 <= nums2:
                nums2 = nums3
            else:
                return True
        return False
        