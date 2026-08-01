class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> index;
        for (int i = 0; i < nums.size(); i++){
            int diff = target-nums[i];
            if (index.count(diff)){
                return {index[diff], i};
            }
            index.insert({nums[i], i});
        }
    }
};
