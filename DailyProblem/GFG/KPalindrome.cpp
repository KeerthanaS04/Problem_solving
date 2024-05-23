#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int kPalindrome(string str,int n,int k){
        vector<int> prev(n+1,0),curr(n+1,0);

        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                if(str[i-1]==str[n-j]){
                    curr[j]=prev[j-1]+1;
                }else{
                    curr[j]=max(prev[j],curr[j-1]);
                }
            }
            swap(prev,curr);
        }
        int lps=prev[n]; //longest palindrome sequence
        int minDeletions=n-lps;
        return minDeletions<=k?1:0;
    }
};