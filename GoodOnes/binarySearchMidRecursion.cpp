#include<bits/stdc++.h>
using namespace std;

void print(int arr[],int start,int end){
    for(int i=start;i<=end;i++){
        cout<<arr[i]<<" ";
    }cout<<endl;
}

bool binarySearch(int arr[],int start,int end,int k){
    cout<<endl;
    print(arr,start,end);
    int mid=start+(end-start)/2;
    cout<<"Value of mid is "<<arr[mid]<<endl;
    //base case
    //if element not found
    if(start>end)
        return false;
    if(arr[mid]==k)
        return true;
    if(arr[mid]<k){
        return binarySearch(arr,mid+1,end,k);
    }else{
        return binarySearch(arr,start,mid-1,k);
    }
}

int main(){
    int arr[11]={2,4,6,10,14,18,22,38,49,55,222};
    int size=11;
    int key=222;

    cout<<"Present or not "<<binarySearch(arr,0,10,key)<<endl; 

    return 0;
}