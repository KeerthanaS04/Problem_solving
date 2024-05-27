#include<bits/stdc++.h>
using namespace std;

constexpr in MOD=1e9+7;
class Solution{
public:
    int checkRecord(int n){
        using ll=long long;
        vector<vector<vector<ll>>> dp(n,vector<vector<ll>>(2,vector<ll>(3)));

        //base cases for first day
        dp[0][0][0]=1; //P
        dp[0][1][0]=1; //A
        dp[0][0][1]=1; //L

        for(int i=1;i<n;i++){
            //for A: append A after sequences that do not contain A('j'==0)
            dp[i][1][0]=(dp[i-1][0][0]+dp[i-1][0][1]+dp[i-1][0][2])%MOD;

            //for L: append L after sequences ending in no L or 1L
            dp[i][0][1]=dp[i-1][0][0] //no L followed by L
            dp[i][0][2]=dp[i-1][0][1] //1L followed by another L
            dp[i][1][1]=dp[i-1][1][0] //no L followed by L, already contains A
            dp[i][1][2]=dp[i-1][1][1] //1L followed by another L, already contains A

            //for P: append P after any sequence
            dp[i][0][0]=(dp[i-1][0][0]+dp[i-1][0][1]+dp[i-1][0][2])%MOD;
            //for sequences that already contain A, append P
            dp[i][1][0]=(dp[i][1][0]+dp[i-1][1][0]+dp[i-1][1][1]+dp[i-1][1][2])%MOD;
        }
        //calculate the final result by summing up all possible sequences of length 'n'
        ll result=0;
        for(int absence=0;absence<2;absence++){
            for(int late=0;late<3;late++){
                result=(result+dp[n-1][absence][late])%MOD;
            }
        }
        return result;
    }
};