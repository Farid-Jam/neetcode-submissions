class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stack;
        std::unordered_map<char, char> map = {{'}', '{'}, {']', '['}, {')', '('}};
        for (char c : s){
            if (map.count(c) && stack.empty()) return false;
            if (map.count(c) && stack.top() == map[c]){
                stack.pop();
            } else{
                stack.push(c);
            }
        }
        return stack.empty();
    }
};
