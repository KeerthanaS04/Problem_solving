#include<bits/stdc++.h>
using namespace std;

class BinaryTreeNode{
    public:
       int data;
       BinaryTreeNode<int> *left;
       BinaryTreeNode<int> *right;

       BinaryTreeNode(int data){
        this->data=data;
        left=NULL;
        right=NULL;
       }
};

void inorder(BinaryTreeNode<int> *root, int &count){
    //base case
    if(root==NULL){
        return;
    }

    inorder(root->left,count);

    //leaf node
    if(root->left==NULL root->right==NULL){
        count++;
    }

    inorder(root->right,count);
}

int noOfLeafNodes(BinaryTreeNode<int> *root){
    int count=0;
    inorder(root,count);
    return count;
}