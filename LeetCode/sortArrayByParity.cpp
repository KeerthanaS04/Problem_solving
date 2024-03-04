#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    vector<int> sortArrayByParity(vector<int>& nums){
        int left=0,right=nums.size()-1;
        while(left<right){
            if(nums[left]%2!=0){
                swap(arr[left],arr[right--]);
            }else{
                left++;
            }
        }
        return nums;
    }
};