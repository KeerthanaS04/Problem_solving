#include<bits/stdc++.h>
#include<stack>
#define MAX 1000
using namespace std;

class Solution{
    private:
    vector<int> nextSmallerElement(int* arr,int n){
        stack<int> s;
        s.push(-1);
        vector<int> ans(n);

        for(int i=n-1;i>=0;i--){
            int curr=arr[i];
            if(s.top()!=-1 && arr[s.top()]>=curr){
                s.pop();
            }
            //ans is at the top of the stack
            ans[i]=s.top();
            s.push(i);
        }
        return ans;
    }

    vector<int> prevSmallerElement(int* arr,int n){
        stack<int> s;
        s.push(-1);
        vector<int> ans(n);

        for(int i=0;i<n>;i++){
            int curr=arr[i];
            if(s.top()!=-1 && arr[s.top()]>=curr){
                s.pop();
            }
            //ans is at the top of the stack
            ans[i]=s.top();
            s.push(i);
        }
        return ans;
    }

    int largestRectangleArea(int* arr,int n){
        vector<int> next(n);
        next=nextSmallerElement(arr,n);

        vector<int> prev(n);
        prev=prevSmallerElement(arr,n);

        int area=INT_MIN;

        for(int i=0;i<n;i++){
            int l=arr[i];

            if(next[i]==-1){
                next[i]=n;
            }
            int b=next[i]-prev[i]-1;
            int newArea=l*b;
            area=max(area,newArea);
        }
        return area;
    }

    public:
    int maxArea(int M[MAX][MAX],int n,int m){
        //compute area for first row
        int area=largestRectangleArea(M[0],m);

        for(int i=1;i<n;i++){
            for(int j=0;j<n;j++){
                //row updating by adding previous row values
                if(M[i][j]!=0){
                    M[i][j]=M[i][j]+M[i-1][j];
                }else{
                    M[i][j]=0;
                }
            }
            //entire row is updating now
            area=max(area,largestRectangleArea(M[i],m));
        }
        return area;
    }
};

int main(){
    int t;
    cin>>t;
    while(t--){
        int n,m;
        cin>>n>>m;

        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                cin>>M[i][j];
            }
        }
        Solution obj;
        cout<<obj.maxArea(M,n,m)<<endl;
    }
}