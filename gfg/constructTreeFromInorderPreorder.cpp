#include<bits/stdc++.h>
using namespace std;

// InOrder = LNR -> Left,Root,Right
// PreOrder = NLR -> Root,Left,Right
struct Node{
    int data;
    Node* left;
    Node* right;
};

class Solution{
    public:
    int findPosition(int in[],int inOrderStart,int inOrderEnd,int element,int n){
        for(int i=inOrderStart;i<inOrderEnd;i++){
            if(in[i]==element)
                return i;
        }
        return -1;
    }
    Node* solve(int in[],int pre[],int &index,int inOrderStart,int inOrderEnd,int n){
        //base case
        if(index>=n || inOrderStart>inOrderEnd){
            return NULL;
        }
        int element=pre[index++];
        Node* root=new Node(element);
        int position=findPosition(in,inOrderStart,inOrderEnd,element,n);

        //recursive calls
        root->left=solve(in,pre,index,inOrderStart,position-1,n);
        root->right=solve(in,pre,index,position+1,inOrderEnd,n);

        return root;
    }
    Node* buildTree(int in[],int pre[],int n){
        int preOrderIndex=0;
        Node* ans=solve(in,pre,preOrderIndex,0,n-1,n);
        return ans;
    }
};