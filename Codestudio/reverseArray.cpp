#include<bits/stdc++.h>
#include<vector>
using namespace std;

void reverseArray(vector<int> &arr,int m){
    int start=m+1; //Given that after the mth position to the end.
    int end=arr.size()-1;
    while(start<=end){
        swap(arr[start],arr[end]);
        start++;
        end--;
    }
}