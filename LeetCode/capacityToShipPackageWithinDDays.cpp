#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    bool isPossible(vector<int>& weights,int n,int days,int mid){
        int count=1;
        int maxWeight=0;
        for(int i=0;i<n;i++){
            if(maxWeight+weights[i]<mid){
                maxWeight+=weights[i];
            }else{
                count++;
                if(count>days || weights[i]>mid){
                    return false;
                }
                maxWeight=weights[i];
            }
            if(count>days){
                return false;
            }
        }
        return true;
    }
    int shipWithinDays(vector<int>& weights, int days){
        int n=weights.size();
        if(n<days){
            return -1;
        }
        int start=0;
        int sum=0;
        for(int i=0;i<n;i++){
            sum+=weights[i];
        }
        int end=sum;
        int mid=start+(end-start)/2;
        while(start<=end){
            if(isPossible(weights,n,days,mid)){
                ans=mid;
                end=mid-1;
            }else{
                start=mid+1;
            }
            mid=start+(end-start)/2;
        }
        return ans;
    }
};