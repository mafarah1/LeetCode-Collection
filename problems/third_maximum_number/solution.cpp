class Solution {
public:
    int thirdMax(vector<int>& nums) {
        int sol = nums[0];
        int max = nums[0];
        int tally = 0;
        //To find the greatest number
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > max) {
                max = nums[i];
            }
        }
        sol = max;
        sort(nums.begin(), nums.end());
        //To find the third greatest
        for (int i = (nums.size() - 1); i >= 0; i--) {
            if (nums[i] < sol) {
                sol = nums[i];
                tally++;
            }
            if (tally == 2) {
                return sol;
                break;
            }
        }
        return max;
    }
};