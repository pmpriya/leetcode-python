public class App {
    public static void main(String[] args) {
        runningSumOf1dArray runningsum = new runningSumOf1dArray();
        // using a test case with left string as 4 and right string as 1000
        int[] numbers = new int[] {3,1,2,10,1};
        int[] output = runningsum.runningSum(numbers);
        System.out.println("Printing for Running Sum of 1D Array: ");
        for(int i = 0; i < numbers.length; i++) {
            System.out.println(output[i]);
        }

    }
}
