#include<bits/stdc++.h>
using namespace std;

int firstOcc(vector<int>& arr,int n,int k){
	int start=0,end=n-1;
	int mid=start+(end-start)/2;
	int ans=-1;
	while(start<=end){
		if(arr[mid]==k){
			ans=mid;
			end=mid-1;
		}else if(arr[mid]<k){
			start=mid+1;
		}else{
			end=mid-1;
		}
		mid=start+(end-start)/2;
	}
	return ans;
}

int lastOcc(vector<int>& arr,int n,int k){
	int start=0,end=n-1;
	int mid=start+(end-start)/2;
	int ans=-1;
	while(start<=end){
		if(arr[mid]==k){
			ans=mid;
			start=mid+1;
		}else if(arr[mid]<k){
			start=mid+1;
		}else{
			end=mid-1;
		}
		mid=start+(end-start)/2;
	}
	return ans;
}

int count(vector<int>& arr, int n, int x) {
	// Write Your Code Here
	int first=firstOcc(arr,n,x);
	int last=lastOcc(arr,n,x);
	int result=last-first+1;
	if(first==-1 && last==-1){
		return 0;
	}else{
		return result;
	}
}
