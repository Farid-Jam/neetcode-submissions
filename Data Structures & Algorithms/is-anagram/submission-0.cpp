class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> counterS;
        unordered_map<char, int> counterT;
        for (int i = 0; i < s.length(); i++){
            counterS[s[i]]++;
        }
        for (int i = 0; i < t.length(); i++){
            counterT[t[i]]++;
        }
        if (counterT == counterS) return true;
        return false;
    }
};
