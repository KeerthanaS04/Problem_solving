#include<bits/stdc++.h>
using namespace std;

int findDuplicate(vector<int>& arr){
    int ans=0;
    for(int i=0;i<arr.size();i++){
        ans^=arr[i];
    }
    for(int i=0;i<arr.size();i++){
        ans^=i;
    }
    return ans;
}