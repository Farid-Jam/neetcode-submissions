class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> res;
        for (const auto& str : strs) {
            vector<int> alphabet(26, 0);
            for (char c : str) {
                alphabet[c - 'a']++;
            }
            string key = to_string(alphabet[0]);
            for (int i = 1; i < 26; ++i) {
                key += ',' + to_string(alphabet[i]);
            }
            res[key].push_back(str);
        }
        vector<vector<string>> result;
        for (const auto& pair : res) {
            result.push_back(pair.second);
        }
        return result;
    }
};
