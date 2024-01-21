#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int ans;
    int solve(Node* root){
        if(!root){
            return 0;
        }
        int left=solve(root->left);
        int right=solve(root->right);
        ans+=abs(left)+abs(right);
        return root->key+left+right-1;
    }

    int distributeCandy(Node* root){
        solve(root);
        return ans;
    }
};