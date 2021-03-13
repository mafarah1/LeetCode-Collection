class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_set<int> nums2;
        for (int n : nums) {
            if (nums2.count(n) > 0) {
                nums2.erase(n);
                continue;
            }
            nums2.insert(n);
        }
        int n;
        for (auto itr = nums2.begin(); itr != nums2.end(); itr++) { 
            n = *itr; 
        }
        return n;
    }
};