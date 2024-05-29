#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int findWinner(int n,int x,int y){
        vector<int> arr(n+1,0);
        arr[1]=1;
        for(i=2;i<=n;i++){
            int j=i-1; //for coin 1
            if(j>=0 && arr[j]==0){
                arr[i]=1;
            }
            j=i-x; // for x coins
            if(j>=0 && arr[j]==0){
                arr[i]=1;
            }
            j=i-y; // for y coins
            if(j>=0 && arr[j]==0){
                arr[i]=1;
            }
        }
        return arr[n];
    }
};