#include<bits/stdc++.h>
using namespace std;

int getPivot(int arr[],int n){
    int start=0,end=n-1;
    int mid=start+(end-start)/2;
    while(start<end){
        if(arr[mid]>=arr[0]){
            start=mid+1;
        }else{
            end=mid;
        }
        mid=start+(end-start)/2;
    }
    return start; //we can return end also
}

int main(){
    int arr[5]={3,8,10,17,1};
    cout<<"Pivot is "<<getPivot(arr,5)<<endl;
}