#include<bits/stdc++.h>
using namespace std;

queue<int> modifyQueue(queue<int> q,int k);

int main(){
    cin>>t;
    while(t-->0){
        int n,k;
        cin>>n>>k;
        queue<int> q;
        while(n-->0){
            int a;
            cin>>a;
            q.push(a);
        }
        queue<int> ans=modifyQueue(q,k);    
        while(!ans.empty()){
            int a=ans.front();
            ans.pop();
            cout<<a<<" ";
        }
        cout<<endl;
    }
}

//Function to reverse first K elements of a queue
queue<int> modifyQueue(queue<int> q,int k){
    //algo
    //step-1: pop first k from q and put into stack
    stack<int> s;
    for(int i=0;i<k;i++){
        int val=q.front();
        q.pop();
        s.push(val);
    }

    //step-2: fetch from stack and push into q
    while(!s.empty()){
        int val=s.top();
        s.pop();
        q.push(val);
    }

    //step-3: fetch first (n-k) elements from q and push back to q
    int t=q.size()-k;
    while(t--){
        int val=q.front();
        q.pop();
        q.push(val);
    }
    return q;
}