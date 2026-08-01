class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        vector<vector<int>> freqCounter(nums.size() + 1);

        for (int n : nums) {
            count[n]++;
        }
        for (const auto& entry : count) {
            freqCounter[entry.second].push_back(entry.first);
        }

        vector<int> res;
        for (int i = freqCounter.size() - 1; i >= 0; --i) {
            for (int num : freqCounter[i]) {
                if (k > 0) {
                    res.push_back(num);
                    k--;
                } else return res;
            }
        }
        return res;
    }
};
