#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int dp[101][101];

    int minFallingPathSum(vector<vector<int>>& matrix){
        int n=matrix.size();
        int m=matrix[0].size();

        for(int i=0;i<m;i++) dp[0][i]=matrix[0][i];
        for(int i=1;i<n;i++){
            for(int j=0;j<m;j++){
                int mini=10005;
                if(i-1>=0) mini=min(mini,dp[i-1][j]);
                if(i-1>=0 && j-1>=0) mini=min(mini,dp[i-1][j-1]);
                if(i-1>=0 && j+1<m) mini=min(mini,dp[i-1][j+1]);

                dp[i][j]=mini+matrix[i][j];
            }
        }
        int ans=dp[n-1][0];
        for(int i=1;i<m;i++) ans=min(ans,dp[n-1][i]);

        return ans;
    }
};