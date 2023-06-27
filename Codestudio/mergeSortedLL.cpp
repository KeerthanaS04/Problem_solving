#include<bits/stdc++.h>
using namespace std;

class node{
    public:
        int data;
        node * next;
        node(int data){
            this->data=data;
            this->next=NULL;
        }
};

node* findMid(Node* head){
    Node* slow=head;
    Node* fast=head->next;

    while(fast!=NULL && fast->next!=NULL){
        slow=slow->next;
        fast=fast->next->next;
    }
    return slow;
}
node* merge(node* left,node* right){
    if(left==NULL)
        return right;
    if(right==NULL)
        return left;

    node* ans=new node(-1);
    node* temp=ans;

    //merge two sorted linked list
    while(left!=NULL && right!=NULL){
        if(left->data<right->data){
            temp->next=left;
            temp=left;
            left=left->next;
        }else{
            temp->next=right;
            temp=right;
            right=right->next;
        }
    }
    while(left!=NULL){
        temp->next=left;
        temp=left;
        left=left->next;
    }
    while(right!=NULL){
        temp->next=right;
        temp=right;
        right=right->next;
    }
    ans=ans->next;
    return ans;
}
node* mergeSort(node *head) {
    // Write your code here.
    //base case
    if(head==NULL || head->next==NULL){
        return head;
    }
    //break LL into two halves, after finding mid
    node* mid=findMid(head);

    node* left=head;
    node* right=mid->next;
    mid->next=NULL;

    //recursive calls to both halves
    left=mergeSort(left);
    right=mergeSort(right);

    //merge both left and right
    node* result=merge(left,right);

    return result;
}
