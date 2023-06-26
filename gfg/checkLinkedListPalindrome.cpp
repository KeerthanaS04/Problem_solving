#include<bits/stdc++.h>
#include<vector>
using namespace std;


struct Node{
    int data;
    struct Node* next;
    Node(int x){
        data=x;
        next=NULL;
    }
};
//Approach 1
class Solution{
    private:
    bool checkPalindrome(vector<int> arr){
        int n=arr.size();
        int start=0;
        int end=n-1;

        while(start<=end){
            if(arr[start]!=arr[end]){
                return 0;
            }
            start++;
            end--;
        }
        return 1;
    }
    public:
    //Function to check whether it is palindrome
    bool isPalindrome(Node* head){
        //copy the array
        vector<int> arr;
        Node* temp=head;
        while(temp!=NULL){
            arr.push_back(temp->data);
            temp=temp->next;
        }
        return checkPalindrome(arr);
    }
};
---------------------------------
class Solution{
    private:
    Node* getMid(Node* head){
        Node* slow=head;
        Node* fast=head->next;

        while(fast!=NULL && fast->next!=NULL){
            fast=fast->next->next;
            slow=slow->next;
        }
        return slow;
    }
    Node* reverse(Node* head){
        Node* curr=head;
        Node* prev=NULL;
        Node* next=NULL;

        while(curr!=NULL){
            next=curr->next;
            curr->next=prev;
            prev=curr;
            curr=next;
        }
        return prev;
    }

    public:
    //function to check whether the list is palindrome
    bool isPalindrome(Node* head){
        if(head->next==NULL){
            return true;
        }
        //step-1: find middle
        Node* middle=getMid(head);
        //step-2: reverse list after middle
        Node* temp=middle->next;
        middle->next=reverse(temp);

        //step-3: compare both halves
        Node* head1=head;
        Node* head2=middle->next;

        while(head2!=NULL){
            if(head1->data!=head2->data){
                return false;
            }
            head1=head1->next;
            head2=head2->next;
        }
        //step-4: return step-2 => temporary one(without this also the code will work)
        temp=middle->next;
        middle->next=reverse(temp);

        return true;
    }
};