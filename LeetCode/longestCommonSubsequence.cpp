#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int longestCommonSubsequence(string text1,string text2){
        int m=text1.size();
        int n=text2.size();

        vector<int> dp(n+1,0);

        for(int i=1;i<=m;i++){
            int dp_is1_js1=dp[0];
            for(int j=1;j<=n;j++){
                int dp_is1_js=dp[j];
                if(text1[i-1]==text[j-1]){
                    dp[j]=dp_is1_js1+1;
                }else{
                    dp[j]=max(dp[j-1],dp[j]);
                }
                dp_is1_js1=dp_is1_js;
            }
        }
        return dp[n];
    }
};