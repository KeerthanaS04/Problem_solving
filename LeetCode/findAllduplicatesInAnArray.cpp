#include<bits/stdc++.h>
using namespace std;
class Solution{
public:
    vector<int> findDuplicates(vector<int>& nums){
        vector<int> ans;
        for(int n:nums){
            n=abs(n);
            if(nums[n-1]>0){
                nums[n-1]*=-1;
            }else{
                ans.push_back(n);
            }
        }
        return ans;
    }
};