# using kadane's algorithm to solve the maximum sum sub-array problem
# time complexity = O(n)

class kadane_algorithm:
    def maxSubArray(self, nums):
        cur_max, max_till_now = 0, -inf
        for c in nums:
            cur_max = max(c, cur_max + c)
            max_till_now = max(max_till_now, cur_max)
        return max_till_now    

if __name__ == '__main__':
    res = kadane_algorithm().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(res)
    # output = 6
