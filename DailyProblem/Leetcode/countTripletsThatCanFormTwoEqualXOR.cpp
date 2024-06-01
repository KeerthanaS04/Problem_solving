#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int countTriplets(vector<int>& arr){
        int n=arr.size();
        vector<int> prefixXOR(n+1);

        for(int i=0;i<n;i++){
            prefixXOR[i+1]=prefixXOR[i]^arr[i];
        }
        int ans=0;

        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                for(int k=j;k<n;k++){
                    int a=prefixXOR[j]^prefixXOR[i];
                    int b=prefixXOR[k+1]^prefixXOR[j];

                    if(a==b){
                        ans++;
                    }
                }
            }
        }
        return ans;
    }
};