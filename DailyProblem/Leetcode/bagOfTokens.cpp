#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int bagOfTokens(vector<int>& tokens,int p){
        sort(tokens.begin(),tokens.end());
        int result=0,points=0;
        int left=0,right=tokens.size()-1;
        while(left<=right){
            if(p>=tokens[left]){
                p-=tokens[left++];
                result=max(result,++points);
            }else if(points>0){
                --points;
                p+=tokens[right--];
            }else{
                break;
            }
        }
        return result;
    }
};