#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    vector<int> money;
    int rob(vector<int>& nums){
        if(nums.size()==0) return 0;
        else if(nums.size()==1) return nums[1];

        int n=nums.size();
        money=nums;
        money.push_back(0);
        for(int i=n-3;i>=0;i--){
            money[i]+=max(money[i+2],money[i+3]);
        }
        return max(money[0],money[1]);
    }
};