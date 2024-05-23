#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int res=0;
    void cal(int idx,vector<int>& nums,int k,int mask){ //bitmasking
        if(idx==nums.size()) {res++; return;}

        bool cant=false;

        for(int i=0;i<idx;i++){
            if(mask&(1<<i)){
                if(abs(nums[i]-nums[idx])==k){
                    cant=true;
                    break;
                }
            }
        }
        // cant is false
        if(!cant) cal(idx+1,nums,k,mask|(1<<idx));
        cal(idx+1,nums,k,mask);
    }
    int beautifulSubsets(vector<int>& nums,int k){
        res=0;
        cal(0,nums,k,0);
        return res-1;
    }
};