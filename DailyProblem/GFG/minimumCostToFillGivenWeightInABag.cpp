#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int minimumCost(int n,int w,vector<int>& cost){
        vector<int> dp(w+1,INT_MAX);
        dp[0]=0;
        for(int i=0;i<n;i++){
            if(cost[i]!=-1){
                for(int j=i+1;j<=w;j++){
                    dp[j]=min(dp[j],cost[i]+dp[j-i-1]);
                }
            }
        }
        return dp[w]!=INT_MAX?dp[w]:-1;
    }
};