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

bool isBST(BinaryTreeNode<int> *root,int min,int max){
    //base case
    if(root==NULL)
        return true;
    
    if(root->data>=min && root->data<=max){
        bool left=isBST(root->left,min,root->data);
        bool right=isBST(root->right,root->data,max);
        return left && right;
    }else
        return false;
}

bool validateBST(BinaryTreeNode<int> *sroot){
    return isBST(root,INT_MIN,INT_MAX);
}