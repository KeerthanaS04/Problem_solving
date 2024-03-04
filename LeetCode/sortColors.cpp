#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    void sortColors(vector<int>& nums){
        int count0=0,count1=0,count2=0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]==0){
                count0++;
            }
            if(nums[i]==1){
                count1++;
            }
        }

        for(int i=0;i<count0;i++){
            arr[i]=0;
        }
        count2=count0+count1;
        for(int i=count0;i<count2;i++){
            arr[i]=1;
        }
        for(int i=count2;i<nums.size();i++){
            arr[i]=2;
        }
    }
};