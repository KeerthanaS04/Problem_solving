#include<bits/stdc++.h>
using namespace std;

class Solution{
    public: 
        int subtractProductAndSum(int n){
            int product=1;
            int sum=0;
            while(n!=0){
                int digit=n%10;
                product*=digit;
                sum+=digit;
                n/=10;
            }
            int res=product-sum;
            return res;
        }
};