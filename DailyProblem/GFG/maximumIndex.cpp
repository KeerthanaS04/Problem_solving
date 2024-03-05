#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int maxIndexDiff(int a[],int n){
        vector<int> prefix(n),suffix(n);
        prefix[0]=a[0];
        suffix[n-1]=a[n-1];
        for(int i=1;i<n;i++){
            prefix[i]=min(prefix[i-1],a[i]);
            suffix[n-i-1]=max(suffix[n-i],a[n-i-1]);
        }
        int i=0,j=0,ans=0;
        while(j<n){
            if(prefix[i]<=suffix[j]){
                ans=max(ans,j-i);
                ++j;
            }else{
                ++i;
            }
        }
        return ans;
    }
};