#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int reverse(int x){
        long long res=0;
        if(x/10==0){
            return x;
        }
        while(x){
            res=res*10+x%10;
            x=x/10;
        }
        return (res<INT_MIN || res>INT_MAX)?0:res;
    }
};