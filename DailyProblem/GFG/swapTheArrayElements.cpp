#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    void swapElements(int arr[],int n){
        if(n<=2) return;
        for(int i=0;i<n-2;i++){
            swap(arr[i],arr[i+2]);
        }
    }
};