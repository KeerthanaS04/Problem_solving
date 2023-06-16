#include <bits/stdc++.h> 
#include<vector>
using namespace std;

int partition(vector<int>& arr,int start,int end){
    int pivot=arr[start];

    int count=0;
    for(int i=start+1;i<=end;i++){
        if(arr[i]<=pivot){
            count++;
        }
    }
    //place a pivot at right position
    int pivotIndex=start+count;
    swap(arr[pivotIndex],arr[start]);

    //balance the right and left part
    int i=start,j=end;
    while(i<pivotIndex && j>pivotIndex){
        while(arr[i]<=pivot){
            i++;
        }
        while(arr[j]>pivot){
            j--;
        }
        if(i<pivotIndex && j>pivotIndex){
            swap(arr[i++],arr[j--]);
        }
    }
    return pivotIndex;
}

void solve(vector<int>& arr,int start,int end){
    //base case
    if(start>=end)
        return ;
    //making partition
    int p=partition(arr,start,end);

    //left part sort
    solve(arr,start,p-1);

    //right part sort
    solve(arr,p+1,end);
}

vector<int> quickSort(vector<int> arr)
{
    solve(arr,0,arr.size()-1);
    return arr;
}
