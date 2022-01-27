# using kadane's algorithm to solve the maximum sum sub-array problem
# time complexity = O(n)

class kadane_algorithm:
    def maxSubArray(self, nums):
        max_till_now = nums[0]
        max_ending = 0

        for i in range(0, len(nums)):
            max_ending = max_ending + nums[i]
            if max_ending < 0:
                max_ending = 0

            elif (max_till_now < max_ending):
                max_till_now = max_ending
        return max_till_now

if __name__ == '__main__':
    res = kadane_algorithm().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(res)
    # output = 6
