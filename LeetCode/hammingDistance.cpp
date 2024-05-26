#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int hammingDistance(int x,int y){
        int diff=x^y;
        int ans=0;
        while(diff){
            ans+=(diff&1)
            diff>>=1;
        }
        return ans;
    }
};