#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    // int count=1;

    int row=1;
    while(row<=n){
        int col=1;
        int value=row;
        while(col<=row){
            cout<<value<<" ";
            value=value+1;
            col=col+1;
        }
        cout<<endl;
        row=row+1;
    }
}