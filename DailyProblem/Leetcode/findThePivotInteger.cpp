#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int pivotInteger(int n){
        for(int i=1;i<=n;i++){
            long long leftSum=(i*(i+1))/2;
            long long rightSum=(n*(n+1))/2-(i*(i-1))/2;

            if(leftSum==rightSum) return i;
        }
        return -1;
    }
};