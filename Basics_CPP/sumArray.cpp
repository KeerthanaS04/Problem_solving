#include<bits/stdc++.h>
using namespace std;

int getSum(int arr[],int n){
    int sum=0;
    for(int i=0;i<n;i++){
        sum+=arr[i];
    }
    return sum;
}

int main(){
    int n;
    cin>>n;

    int arr[100];

    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    cout<<"Sum of the elements in the array is "<<getSum(arr,n)<<endl;
}