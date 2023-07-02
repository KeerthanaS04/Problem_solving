#include<bits/stdc++.h>
#include<stack>
using namespace std;

void insertAtBottom(stack<int> &s,int element){
    //base case
    if(s.empty()){
        s.push(element);
        return;
    }

    int num=s.top();
    s.pop();

    //recursive call
    insertAtBottom(s, element);

    s.push(num);
}

void reverseStack(stack<int> &stack) {
    // Write your code here
    if(stack.empty()){
        return;
    }
    int num=stack.top();
    stack.pop();

    //recursive call
    reverseStack(stack);

    insertAtBottom(stack, num);
}