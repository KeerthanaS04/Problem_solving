#include<bits/stdc++.h>
using namespace std;

struct Node{
    int data;
    struct Node* right;
    struct Node* left;

    Node(int x){
        data=x;
        left=right=NULL;
    }
};

class Solution{
    public:
    void solve(Node* root,int sum,int &maxSum,int len,int &maxlen){
        //base case
        if(root==NULL){
            if(len>maxlen){
                maxlen=len;
                maxSum=sum;
            }else if(len==maxlen){
                maxSum=max(maxSum,sum);
            }
            return;
        }

        solve(root->left,sum,maxSum,len+1,maxlen);
        solve(root->right,sum,maxSum,len+1,maxlen);
    }
    int sumOfLongRootToLeafPath(Node* root){
        int len=0;
        int maxlen=0;

        int sum=0;
        int maxSum=INT_MIN;

        solve(root,sum,maxSum,len,maxlen);

        return maxSum;
    }
};