class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> ans;
        int L = 0;
        int R = numbers.size() - 1;
        while (L < R){
            if (numbers[L] + numbers[R] < target){
                L++;
            } else if (numbers[L] + numbers[R] > target){
                R--;
            }
            else {
                ans.push_back(L+1);
                ans.push_back(R+1);
                return ans;
            }
        }
        return ans;
    }
};
