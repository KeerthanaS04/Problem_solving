#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    bool valid(int x,int y,int n){
        if(x>=0&&x<n&&y>=0&&y<n) return true;
        else return false;
    }
    vector<int> matrixDiagonally(vector<vector<int>>& mat){
        int n=mat.size();
        vector<int> ans;
        int temp=0;
        for(int j=0;j<n;j++){
            int x=0;
            int y=j;
            int presentSize=ans.size();
            while(valid(x,y,n)){
                ans.push_back(mat[x][y]);
                x++;
                y--;
            }
            if(temp%2==0){
                reverse(ans.begin()+presentSize,ans.end());
            }
            temp++;
        }

        for(int i=1;i<n;i++){
            int x=i;
            int y=n-1;
            int presentSize=ans.size();
            while(valid(x,y,n)){
                ans.push_back(mat[x][y]);
                x++;
                y--;
            }
            if(temp%2==0){
                reverse(ans.begin()+presentSize,ans.end());
            }
            temp++;
        }
        return ans;
    }
};