#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int pivotIndex(vector<int>& nums){
        int total=0;
        int leftSum=0;
        for(int i=0;i<nums.size();i++){
            total+=nums[i];
        }
        for(int i=0;i<nums.size();i++){
            total-=nums[i];
            if(leftSum==total){
                return i;
            }
            leftSum+=nums[i];
        }
        return -1;
    }
};