
# leetcode problem 1470. Shuffle the Array
# Runtime 64 ms

class shuffle_array:
    def shuffle(self, nums, n):
        newarr = [nums[i] for i in range(n,len(nums))]
        res = []
        count1 = 0
        count2 = 0
        for i in range(0, len(nums)):
            if(i%2 == 0):
                res.append(nums[count1])
                count1 = count1+1
            else:
                res.append(newarr[count2])
                count2=count2+1
        return res

if __name__ == '__main__':
    output = shuffle_array([1,2,3,4,4,3,2,1], 4)
    print(output)