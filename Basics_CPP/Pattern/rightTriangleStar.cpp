#include<bits/stdc++.h>
using namespace std;

int main(){
    int n=1;
    cin>>n;

    int row=1;
    while(row<=n){
        //printing space
        int space=n-i;
        while(space){
            cout<<" ";
            space=space-1;
        }
        //printing star
        int col=1;
        while(col<=row){
            cout<<"*";
            col=col+1;
        }
        cout<<endl;
        row=row+1;
    }
}