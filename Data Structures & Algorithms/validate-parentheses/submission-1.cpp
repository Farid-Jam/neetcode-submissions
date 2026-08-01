class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        for (char ch : s){
            if (st.empty() && !(ch == '{' || ch == '[' || ch == '(')) return false;
            if (ch == '{' || ch == '[' || ch == '('){
                st.push(ch);
            } else {
                if (st.top() == '{'){
                    if (ch != '}') return false;
                    st.pop();
                }
                else if (st.top() == '('){
                    if (ch != ')') return false;
                    st.pop();
                } else {
                    if (ch != ']') return false;
                    st.pop();
                }
            }
        }
        return st.empty();
    }
};
