#include<bits/stdc++.h>
using namespace std;

class BinaryTreeNode{
    public:
        int data;
        BinaryTreeNode<int> *left,*right;
        BinaryTreeNode() :data(0),left(NULL),right(NULL){}
        BinaryTreeNode(int,x) :data(x),left(NULL),right(NULL){}
        BinaryTreeNode(int x,BinaryTreeNode<int> *left,BinaryTreeNode<int> *right) :data(x),left(left),right(right){}
};

bool searchInBST(BinaryTreeNode<int> *root,int x){
    BinaryTreeNode<int> *temp=root;
    while(temp!=NULL){
        //base case
        if(temp->data==x){
            return true;
        }
        if(temp->data>x){
            temp=temp->left;
        }else{
            temp=temp->right;
        }
    }
    return false;
}