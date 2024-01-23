#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    vector<vector<int>> pathSum(TreeNode* root,int targetSum){
        vector<vector<int>> ans;
        help(root,targetSum,{},ans);
        return ans;
    }

private:
    void help(TreeNode* root,int targetSum,vector<int>&& path,vector<vector<int>>& ans){
        if(root==nullptr) return;
        if(root->val==targetSum && root->left==nullptr && root->right==nullptr){
            path.push_back(root->val);
            ans.push_back(path);
            path.pop_back();
            return;
        }
        path.push_back(root->val);
        help(root->left,targetSum,move(path),ans);
        help(root->right,targetSum,move(path),ans);
        path.pop_back();
    }
};