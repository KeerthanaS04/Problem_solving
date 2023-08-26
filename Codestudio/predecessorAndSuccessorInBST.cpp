#include<bits/stdc++.h>
using namespace std;

class TreeNode{
    public:
        int data;
        TreeNode *left,*right;
        TreeNode():data(0),left(NULL),right(NULL){}
        TreeNode(int x):data(x),left(NULL),right(NULL){}
        TreeNode(int x,TreeNode *left,TreeNode *right):data(x),left(left),right(right){}
};

pair<int,int> predecessorSuccessor(TreeNode<int>* root,int key){
    //find key
    TreeNode<int>* temp=root;
    int pred=-1;
    int succ=-1;

    while(temp->data!=key){
        if(temp->data>key){
            succ=temp->data;
            temp=temp->left;
        }else{
            pred=temp->data;
            temp=temp->right;
        }
    }

    //pred and succ

    //pred
    TreeNode<int>* leftTree=temp->left;
    while(leftTree!=NULL){
        pred=leftTree->data;
        leftTree=leftTree->right;
    }

    //succ
    TreeNode<int>* rightTree=temp->right;
    while(rightTree!=NULL){
        succ=rightTree->data;
        rightTree=rightTree->left;
    }

    pair<int,int> ans=make_pair(pred,succ);
    return ans;
    //return {pred,succ};
}