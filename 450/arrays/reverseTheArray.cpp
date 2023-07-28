#include<bits/stdc++.h>
using namespace std;

//function to reverse array from start to end

void reverseArray(int arr[],int start,int end){
    while(start<end){
        int temp=arr[start];
        arr[start]=arr[end];
        arr[end]=temp;
        start++;
        end--;
    }
}
/*
//if reverse start from a specific position
void reverseArray(vector<int> &arr,int m){
    int start=m+1;
    int end=arr.size()-1;
    while(start<=end){
        swap(arr[start],arr[end]);
        start++;
        end--;
    }
}
*/

void printArray(int arr[],int n){
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

int main(){
    int arr[]={1,2,3,4,5,6,7,8,9};

    int n=sizeof(arr)/sizeof(arr[0]);

    //to print original array
    printArray(arr,n);

    //function calling
    reverseArray(arr,0,n-1);

    cout<<"reversed Array is "<<endl;

    //To print the reversed array
    printArray(arr,n);

    return 0;
}
