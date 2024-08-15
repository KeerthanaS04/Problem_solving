#include<bits/stdc++.h>
using namespace std;

struct Node{
    int data;
    struct Node* next;
    Node(int x){
        data = x;
        next = NULL;
    }
};

class Solution{
    public:
    //Function to rotate a linked list
    Node* rotate(Node* head, int k){
        Node* curr = head;
        int n = 0;

        while(curr!=NULL){
            n++;
            curr = curr->next;
        }

        curr = head;
        k = k % n;
        if(k==0) return head;
        for(int i=0;i<k-1;i++){
            curr = curr->next;
        }
        Node* new_head = curr->next;
        curr->next = NULL;

        curr = new_head;
        while(curr->next!=NULL) curr = curr->next;
        curr->next = head;

        return new_head;
    }
};