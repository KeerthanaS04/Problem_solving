#include<bits/stdc++.h>
#include<vector>
using namespace std;

class Solution{
    public:
       void rotate(vector<int>& nums,int k){
        //To not make overwrite we are creating temp 
        vector<int> temp(nums.size());
        for(int i=0;i<nums.size();i++){
            temp[(i+k)%nums.size()]=nums[i];
        }
        //copy temp to nums
        nums=temp;
       }
};