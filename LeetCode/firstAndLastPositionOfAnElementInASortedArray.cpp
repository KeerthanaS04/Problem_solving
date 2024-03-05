#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int firstOcc(vector<int>& nums,int target){
        int start=0,end=nums.size()-1;
        int mid=start+(end-start)/2;
        int ans=-1;
        while(start<=end){
            if(nums[mid]==target){
                ans=mid;
                end=mid-1;
            }else if(nums[mid]<target){
                start=mid+1;
            }else{
                end=mid-1;
            }
            mid=start+(end-start)/2;
        }
        return ans;
    }

    int lastOcc(vector<int>& nums,int target){
        int start=0,end=nums.size()-1;
        int mid=start+(end-start)/2;
        int ans=-1;
        while(start<=end){
            if(nums[mid]==k){
                ans=mid;
                start=mid+1;
            }else if(nums[mid]<k){
                start=mid+1;
            }else{
                end=mid-1;
            }
            mid=start+(end-start)/2;
        }
        return ans;
    }
    
    vector<int> searchRange(vector<int>& nums,int target){
        vector<int> p;
        p.push_back(firstOcc(nums,target));
        p.push_back(lastOcc(nums,target));

        return p;
    }
};