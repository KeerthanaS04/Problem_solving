#include<bits/stdc++.h>
using namespace std;

struct Node{
    int data;
    Node* right;
    Node* left;
};

void createMapping(int n[],map<int,int> &nodeToIndex,int n){
    for(int i=0;i<n;i++){
        nodeToIndex[in[i]]=i;
    }
}

Node* solve(int in[],int post[],int &index,int inOrderStart,int inOrderEnd,int n,map<int,int> &nodeToIndex){
    //base case
    if(index<0 || inOrderstart>inOrderEnd){
        return NULL;
    }

    //create a root node for element
    int element=post[index--];
    Node* root=new Node(element);

    //Find element's index in post order
    int position=nodeToIndex[element];

    //recursive calls
    root->right=solve(in,post,index,inOrderStart,position-1,n,nodeToIndex);
    root->left=solve(in,pre,index,position+1,inOrderEnd,n,nodeToIndex);

    return root;
}

Node* buildTree(int in[],int post[],int n){
    int postOrderIndex=n-1;
    map<int,int> nodeToIndex;

    //create nodes to index mapping
    createMapping(in,nodeToIndex,n);

    Node* ans=solve(in,post,postOrderIndex,0,n-1,n,nodeToIndex);
    return ans;
}