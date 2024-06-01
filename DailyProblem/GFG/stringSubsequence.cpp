#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int MOD=1e9+7;
    int help(string s1,string s2,int i,int j,vector<vector<int>> &dp){
        if(j==s2.length()) return 1;
        if(i==s1.length()) return 0;
        if(dp[i][j]!=-1) return dp[i][j];

        int x=0,y=0;
        if(s1[i]==s2[j]) x=help(s1,s2,i+1,j+1,dp);
        y=help(s1,s2,i+1,j,dp);
        return dp[i][j]=(x+y)%MOD;
    }

    int countWays(string s1,string s2){
        vector<vector<int>> dp(s1.length(),vector<int> (s2.length(),-1))
        return help(s1,s2,0,0,dp);
    }
};