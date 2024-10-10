#include<bits/stdc++.h>
using namespace std;

void validating(char c,stack<char>& st)
{

    
    if(st.empty()){
        st.push(c);
    }
    else{
        if(c == ')'){
            if(st.top() == '('){
                st.pop();
            }
        }
        else if(c == ']'){
            if(st.top() == '['){
                st.pop();
            }
        }
        else if(c == '}'){
            if(st.top() == '{'){
                st.pop();
            }
        }
        else{
            st.push(c);
        }
    }
}
int main(){
    stack<char> st;
    string s;
    cout<<"Input= ";
    cin>>s;
    for(int i=0;i<s.size();i++){
        validating(s[i],st);
    }
    if(st.empty()){
        cout<<"True";
    }
    else{
        cout<<"False";
    }
}