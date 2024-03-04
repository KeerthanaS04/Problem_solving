#include<bits/stdc++.h>
using namespace std;

int binarySearch(int arr[],int size,int k){
    int start=0;
    int end=size-1;
    int mid=start+(end-start)/2;

    while(start<=end){
        if(arr[mid]==k){
            return mid;
        }

        if(key>arr[mid]){
            start=mid+1;
        }else{
            end=mid-1;
        }
        mid=start+(end-start)/2;
    }
    return -1;
}

int main(){
    int even[6]={2,4,6,8,12,18};
    int odd[5]={3,8,11,14,16};

    int oddIndex=binarySearch(even,6,12);
    cout<<"Index of 12 is "<<oddIndex<<endl;

    int evenIndex=binarySearch(odd,5,16);
    cout<<"Index of 16 is "<<evenIndex<<endl;

    return 0;
}