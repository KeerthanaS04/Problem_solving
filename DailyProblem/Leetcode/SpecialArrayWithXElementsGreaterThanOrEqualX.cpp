#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int specialArray(vector<int>& nums){
        int n=nums.size();
        sort(nums.begin(),nums.end());

        int curr=0;
        for(int x=0;x<=n;x++){
            while(curr<n && nums[curr]<x){
                ++curr;
            }
            if(n-curr==x) return x;
        }
        return -1;
    }
};