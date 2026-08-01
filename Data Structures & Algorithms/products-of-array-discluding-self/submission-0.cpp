class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int zeroCount = 0;
        int product = 1;
        for (int num : nums) {
            if (num) {
                product *= num;
            } else zeroCount++;
        }

        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == 0) {
                zeroCount--;
                if (zeroCount) {
                    nums[i] = 0;
                } else nums[i] = product;
                zeroCount++;
            } else {
                if (zeroCount) {
                    nums[i] = 0;
                } else nums[i] = product / nums[i];
            }
        }
        return nums;
    }
};
