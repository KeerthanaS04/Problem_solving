#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;

    int row=1;
    while(row<=n){
        int col=1;
        int space=row-1;
        while(space){
            cout<<" ";
            space=space-1;
        }
        int star=n-row+1;
        while(star){
            cout<<"*";
            star=star-1;
            col=col+1;
        }
        cout<<endl;
        row=row+1;
    }
}