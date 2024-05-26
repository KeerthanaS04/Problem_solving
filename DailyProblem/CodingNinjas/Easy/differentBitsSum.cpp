#include<bits/stdc++.h>
using namespace std;

int differentBitsSumPairwise(vector<int>& arr,int n){
    int ans=0;
    int mod=1000000007;
    int count=1;

    for(int i=0;i<31;i++){
        int co=0;
        int cz=0;
        for(int j=0;j<n;j++){
            int temp=arr[j]&count;
            if(temp==count)co++;
            else cz++;
        }
        ans=(ans%mod+(2*co*cz)%mod)%mod;
        count=count<<1;
    }
    return ans;
}