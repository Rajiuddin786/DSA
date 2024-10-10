#include<bits/stdc++.h>
using namespace std;

class Solution{
    bool validchange(vector<int>& num){
        int minus5,minus10,minus20,min=(*(max_element(num.begin(),num.end()))),flag=-1,flag5=1,flag10=1,flag20=1;
        unordered_map<int,int> pocket = {
            {5,0},
            {10,0},
            {20,0}
        };
        for(int i:num){
            while(i !=0){
                minus5 = i - 5;
                minus10 = i - 10;
                minus20 = i - 20;
                if(minus5 == 0){
                    pocket[5]++;
                    i=0;
                    flag = -1;
                }
                else{
                    if(minus5>0)
                    {
                        if(min>minus5){
                        min=minus5;
                        flag=5;
                        }
                    }
                    else{
                        flag5 = -1;
                    }
                }
                if(minus10 == 0){
                    pocket[10]++;
                    i=0;
                    flag = -1;
                }
                else{
                    if(minus10>0){
                    if(min>minus10){
                        min=minus10;
                        flag=10;
                    }
                    }
                }
                if(minus20 == 0){
                    pocket[20]++;
                    i=0;
                    flag = -1;
                }
                else{
                    if(minus20>0){
                    if(min>minus20){
                        min=minus20;
                        flag=20;
                    }
                    }
                    else{
                        flag20=-1;
                    }
                }
                if(flag == 5){
                        pocket[5]++;
                        i=min;
                    }
                else if(flag == 10){
                        pocket[10]++;
                        i=min;
                    }
                else if(flag == 20){
                        pocket[20]++;
                        i=min;
                    }
            }
        }
    }
};

int main(){
    Solution ob;
    vector<int> num={5,5,10,15};
    cout<<(ob.validchange(num) ? "True" : "False")<<endl;
}