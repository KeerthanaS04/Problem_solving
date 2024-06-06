#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    bool isPossibleDivide(vector<int>& nums,int k){
        //Create a map to count the frequency of each num
        unordered_map<int,int> counts;
        for(int num:nums){
            ++counts[num]; //Increment the count for each num
        }
        //Sort the nums in ascending order
        sort(nums.begin(),nums.end());
        //Treavers through the sorted nums
        for(int num:nums){
            //If the current num is still in the count map(i.e, needed to form a group)
            if(counts.count(num)){
                //Attempt to create a group starting with the current num
                for(int nextNum=num;nextNum<num+k;nextNum++){
                    //If the nextNum is missing in the sequence, can't form a group
                    if(!counts.count(num)){
                        return false;
                    }
                    //Decrement count for the current num in the sequence
                    if(--counts[nextNum]==0){
                        counts.erase(nextNum); //Remove the num from the count map if count reaches zero
                    }
                }
            }
        }
        //If all the nums can be grouped, return true
        return true;
    }
};