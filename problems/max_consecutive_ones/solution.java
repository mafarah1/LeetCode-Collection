class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int keeptrack = 0;
        int solution = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                keeptrack++;
                solution = Math.max(solution, keeptrack);
            } else if (nums[i] != 1) {
                keeptrack = 0;
            }
        }
        return solution;
    }
}