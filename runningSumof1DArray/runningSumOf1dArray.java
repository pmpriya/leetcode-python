public class runningSumOf1dArray {
    public int[] runningSum(int[] nums) {
        int[] array = new int[nums.length];
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            array[i] = sum;
        }
        return array;
    }
}   
