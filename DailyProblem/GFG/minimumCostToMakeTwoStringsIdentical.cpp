#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int LCA(string x,int n1,string y,int n2){
        int dp[n1+1][n2+1];

        for(int i=0;i<=n1;i++){
            for(int j=0;j<=n2;j++){
                if(i==0 || j==0) dp[i][j]=0;
                else if(x[i-1]==y[j-1]) dp[i][j]=1+max(dp[i-1][j-1]);
                else dp[i][j]=max(dp[i-1][j],dp[i][j-1]);
            }
        }
        return dp[n1][n2];
    }
    int findMinCost(string x,string y,int costX,int costY){
        int n1=x.length();
        int n2=y.length();

        int lca=LCA(x,n1,y,n2);
        int minCost=costX*(n1-lca)+costY*(n2-lca);

        return minCost;
    }
};