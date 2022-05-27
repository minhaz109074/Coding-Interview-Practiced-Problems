class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n
        left, right = 1, 1
        #[1,2,3,4]   for val 3 the left part  has 1*2 and right part has 4, ans = left*right,i.e ans = 2*4 = 8
        #left = [1,1,2,6] for every nums[i] we calculate it's left part,such as  for [1,2,3,4] -> [ , 1(2's left product), 2(3's left product), 6(4's left product)]
        # the first value which is empty, we replaced it with 1
        # similar process we will do for right part
        # right = [24(1's right prod),12(2's right prod),4(3's right prod),1(we just replaced the empty part by 1, since 4 has no right prod)]
        # instead of using two separate loop for left and right value calculation, we just did it
        # in one single pass by using another pointer n-1-i from reverse for right values
        # right value will be calculated from end of the array and left value will be calculated from starting point
        # ans[i]*left and ans[n-1-i]*right , so left and right values simultaneously mutiplied in the output array
        for i in range(n):
            ans[i] *= left
            left = left*nums[i]
            ans[n-1-i] *= right     
            right = right*nums[n-1-i]

        return ans
