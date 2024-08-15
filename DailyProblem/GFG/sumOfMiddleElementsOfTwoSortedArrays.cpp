#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int sumOfMiddleElements(vector<int>& arr1, vector<int>& arr2){
        int n = arr2.size();
        int i=0,j=0,m1=-1,m2=-1;
        for(int count=0;count<n;count++){
            if(i==n){
                m1 = m2;
                m2 = arr2[0];
                break;
            }else if(j==n){
                m1 = m2;
                m2 = arr1[0];
                break;
            }
            if(arr1[i]<=arr2[j]){
                m1 = m2;
                m2 = arr1[i];
                i++;
            }else{
                m1 = m2;
                m2 = arr2[j];
                j++;
            }
        }
        return m1+m2;
    }
};