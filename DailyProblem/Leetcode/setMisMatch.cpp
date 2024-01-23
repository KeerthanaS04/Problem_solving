#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    vector<int> findErrorNums(vector<int>& nums){
        vector<int> count(nums.size()+1);
        int rep=-1;
        int loss=-1;
        for(int i=0;i<nums.size();i++){
            count[nums[i]]++;
        }
        for(int i=1;i<count.size();i++){
            if(count[i]==0) loss=i;
            else if(count[i]==2) rep=i;
        }
        return vector<int> {rep,loss};
    }
}
