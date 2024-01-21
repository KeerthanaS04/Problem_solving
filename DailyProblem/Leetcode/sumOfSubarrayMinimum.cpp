#include<bits/stdc++.h>
using namespace std;

class Solution{
public: 
    int sumSubarrayMins(vector<int>& A){
        int n=A.size();
        int MOD=1e9+7;
        vector<int> left(n),right(n);

        //Left Stack
        stack<int> Left_st;
        Left_st.push(0);
        left[0]=1;
        for(int i=1;i<n;i++){
            while(!Left_st.empty() && A[i]<A[Left_st.top()])
                Left_st.pop();
            if(Left_st.empty())
                left[i]=i+1; //Total distance if less element not found=i+1
            else
                left[i]=i-left-st.top(); //distance=i-left-st.top()
            Left_st.push(i);
        }

        //Right Stack
        stack<int> Right_st;
        Right_st.push(n-1);
        right[n-1]=1;
        for(int i=n-2;i>=0;i--){
            while(!Right_st.empty() && A[i]<=A[Right_st.top()])
                Right_st.top();
            if(Right_st.empty())
                right[i]=n-i; //distance
            else
                Right_st.top()-i;
            Right_st.push(i);
        }
        //For each value we have left and right contribution will be (left*right)*element
        long long int res=0;
        for(int i=0;i<n;i++){
            long long prod=(left[i]*right[i])%MOD
            long long net=A[i]*prod;
            res=(res+net)%MOD;
        }
        return res%MOD;
    }
};