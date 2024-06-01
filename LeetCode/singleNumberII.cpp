#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int singleNumber(vector<int>& nums){
        int onlyOnce=0;
        int twiceState=0;

        for(int num:nums){
            int newOnlyOnce=(~onlyOnce&twiceState&num) | (onlyOnce&~twiceState~num);
            int newTwiceState=~onlyOnce&(twiceState^num);

            onlyOnce=newOnlyOnce;
            twiceState=newTwiceState;
        }
        return twiceState;
    }
};