class Solution {
    public int maxProduct(int[] nums) {
        int maxSoFar = nums[0];
        int minSoFar = nums[0];
        int result = nums[0];

        for (int i = 1; i < nums.length; i++) {
            int num = nums[i];

            int tempMax = Math.max(num, Math.max(num * maxSoFar, num * minSoFar));
            int tempMin = Math.min(num, Math.min(num * maxSoFar, num * minSoFar));

            maxSoFar = tempMax;
            minSoFar = tempMin;

            result = Math.max(result, maxSoFar);
        }

        return result;
    }
}