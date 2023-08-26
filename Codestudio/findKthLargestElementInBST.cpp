#include<bits/stdc++.h>
using namespace std;

class BinaryTreeNode{
    public:
        int data;
        BinaryTreeNode<int>* left;
        BinaryTreeNode<int>* right;

        BinaryTreeNode(int data){
            this->data=data;
            left=NULL;
            right=NULL;
        }
};

int solve(BinaryTreeNode<int>* root,int& i,int k){
    //base case
    if(root==NULL){
        return -1;
    }

    //R
    int right=solve(root->right,i,k);

    if(right!=-1){
        return right;
    }

    //N
    i++;
    if(i==k){
        return root->data;
    }

    //L
    return solve(root->left,i,k);
}

int kthSmallest(BinaryTreeNode<int>* root,int k){
    int i=0;
    int ans=solve(root,i,k);
}