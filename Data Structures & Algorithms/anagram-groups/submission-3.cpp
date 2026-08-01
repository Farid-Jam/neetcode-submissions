class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;
        for (string str : strs){
            int alphabet[26] = {0};
            for (char c : str){
                alphabet[c - 'a']++;
            }
            string key = to_string(alphabet[0]);
            for (int i = 1; i < 26; i++){
                key += ',' + to_string(alphabet[i]);
            }
            groups[key].push_back(str);
        }
        vector<vector<string>> res;
        for (const auto& pair : groups){
            res.push_back(pair.second);
        }
        return res;
    }
};
