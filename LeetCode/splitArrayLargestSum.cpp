#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    bool isPossible(vector<int>& nums,int n,int k,int mid){
        int count=1;
        int largeSum=0;
        for(int i=0;i<n;i++){
            if(largeSum+nums[i]<=mid){
                largeSum+=nums[i];
            }else{
                count++;
                if(count>k || nums[i]>mid){
                    return false;
                }
                largeSum=nums[i];
            }
            if(count>k){
                return false;
            }
        }
        return true;
    }
    int splitArray(vector<int>& nums,int k){
        int n=nums.size();
        if(n<k){
            return -1;
        }
        int start=0;
        int sum=0;
        for(int i=0;i<n;i++){
            sum+=nums[i];
        }
        int end=sum;
        int ans=-1;
        int mid=start+(end-start)/2;
        while(start<=end){
            if(isPossible(nums,n,k,mid)){
                ans=mid;
                end=mid-1;
            }else{
                start=mid+1;
            }
            mid=start+(end-start)/2;
        }
        return ans;
    }
};