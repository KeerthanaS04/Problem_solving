#include<bits/stdc++.h>
#include<queue>
using namespace std;

class Solution{
    public:
    queu<int> rev(queue<int> q){
        stack<int> s;

        while(!q.empty()){
            int element=q.front();
            q.pop();
            s.push(element);
        }

        while(!s.empty()){
            int element=s.top();
            s.pop();
            q.push(element);
        }
        return q;
    }
};

int main(){
    int test;
    cin>>test;
    while(test--){
        queue<int> q;
        int n,var;
        cin>>n;
        while(n--){
            cin>>var;
            q.push(var);
        }
        Solution ob;
        queue<int> a=ob.rev(q);
        while(!a.empty()){
            cout<<a.front()<<" ";
            a.pop();
        }
        cout<<endl;
    }
}