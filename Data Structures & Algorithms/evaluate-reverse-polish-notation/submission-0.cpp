class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        for (string token : tokens){
            if (token == "+"){
                int x = st.top();
                st.pop();
                int y = st.top();
                st.pop();
                st.push(y + x);
            } else if (token == "-"){
                int x = st.top();
                st.pop();
                int y = st.top();
                st.pop();
                st.push(y - x);
            } else if (token == "*"){
                int x = st.top();
                st.pop();
                int y = st.top();
                st.pop();
                st.push(y * x);
            } else if (token == "/"){
                int x = st.top();
                st.pop();
                int y = st.top();
                st.pop();
                st.push(y / x);
            } else {
                st.push(stoi(token));
            }
        }
        return st.top();
    }
};
