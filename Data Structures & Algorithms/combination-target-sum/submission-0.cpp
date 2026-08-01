class Solution {
private:
    void dfs(vector<int>& nums, int i, int target, vector<vector<int>>& res, vector<int> combination, int currSum){
        if (currSum > target) return;
        if (currSum == target){
            res.push_back(combination);
        }
        for (int j = i; j < nums.size(); j++){
            combination.push_back(nums[j]);
            dfs(nums, j, target, res, combination, currSum + nums[j]);
            combination.pop_back();
        }
    }
public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        vector<int> combination;
        dfs(nums, 0, target, res, combination, 0);
        return res;
    }
};
