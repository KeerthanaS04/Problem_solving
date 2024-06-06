#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int lengthOfLIS(vector<int>& nums){
        int n=nums.size();
        if(n==0) return 0;
        vector<int> top;
        for(int poker:nums){
            int left=0,right=top.size()-1;
            while(left<=right){
                int mid=left+(right-left)/2;
                if(poker<top[mid]){
                    right=mid-1;
                }else if(poker==top[mid]){
                    right=mid-1;
                }else{
                    left=mid+1;
                }
            }
            if(left==top.size()){
                top.push_back(poker);
            }else{
                top[left]=poker;
            }
        }
        return top.size();
    }
};