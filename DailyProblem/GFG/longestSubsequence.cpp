#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int longestSubsequence(int n,vector<int>& a){
        int ans=0;
        unordered_map<int,int> mm;
        for(int i=0;i<n;i++){
            mm[a[i]]=max(mm[a[i]-1],mm[a[i]+1])+1;
            ans=max(ans,mm[a[i]]);
        }
        return ans;
    }
};