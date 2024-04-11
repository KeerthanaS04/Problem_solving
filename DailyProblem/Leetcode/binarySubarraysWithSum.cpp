#include<bits/stdc++.h>
using namespace std;

class Solution{
private:
    int atmost(vector<int>& nums,int goal){
        int sum=0;
        int start=0,end=0,count=0;
        while(end<nums.size()){
            sum+=nums[ends++];
            while(start<end && sum>goal) sum-=nums[start++];
            count+=end-start;
        }
        return count;
    }

public:
    int numSubarraysWithSum(vector<int>& nums,int goal){
        return atmost(nums,goal)-atmost(nums,goal-1);
    }
};