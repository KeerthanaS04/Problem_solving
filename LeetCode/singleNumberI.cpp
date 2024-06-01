#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int singleNumber(vector<int>& nums){
        int total_xor=0;
        for(int num:nums){
            total_xor^=num;
        }
        return total_xor;
    }
};