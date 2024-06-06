#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int findSwapValues(int a[],int n,int b[],int m){
        int suma=0,sumb=0;
        for(int i=0;i<n;i++) suma+=a[i];
        for(int i=0;i<n;i++) sumb+=b[i];
        if((suma-sumb)%2!=0) return -1;
        int i=0,j=0;
        int target=(suma-sumb)/2;
        sort(a,a+n);
        sort(b,b+m);
        /*
        suma-x+y=sumb+x-y
        => x-y=(suma-sumb)/2
        */
        while(i<n && j<m){
            int diff=a[i]-b[j];
            if(target==diff) return 1;
            else if(target<diff) i++;
            else j++;
        }
        return -1;
    }
};