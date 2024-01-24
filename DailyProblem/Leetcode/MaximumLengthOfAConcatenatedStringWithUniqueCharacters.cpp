#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int maxLength(vector<string>& arr){
        int ans=0;
        int n=arr.size();
        for(int i=0;i<<n;i++){
            int curr_ans=0;
            vector<int> f(26,0);
            for(int j=0;j<n;j++){
                if((i>>j)&1){
                    curr_ans+=arr[j].size();

                    for(auto x:arr[j]){
                        ++f[x-'a'];
                    }
                }
            }
            bool ok=1;
            for(auto x:f){
                if(x>1){
                    ok=0;
                    break;
                }
            }
            if(ok)
                ans=max(ans,curr_ans);
        }
        return ans;
    }
};