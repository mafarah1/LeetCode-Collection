class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> hash;
        for (int k : nums) {
            if (hash.count(k) > 0) {
                return true;
            }
            hash.insert(k);
        }
        return false;
    }
};