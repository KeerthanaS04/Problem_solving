#include<bits/stdc++.h>
using namespace std;

class LinkedListNode{
    public:
    int data;
    LinkedListNode<int> *next;
    LinkedListNode(int data){
        this->data=data;
        this->next=NULL;
    }
};

LinkedListNode<int> *reverseLinkedList(LinkedListNode<int> *head){
    //if it is empty or containing one element only
    if(head==NULL || head->next==NULL){
        return head;
    }
    LinkedListNode<int>* curr=head;
    LinkedListNode<int>* prev=NULL;
    LinkedListNode<int>* forward=NULL;

    while (curr!=NULL)
    {
        forward=curr->next;
        curr->next=prev;
        prev=curr;
        curr=forward;
    }
    return prev;
    
}