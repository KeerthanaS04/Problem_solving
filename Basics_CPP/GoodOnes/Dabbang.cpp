#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;

    int row=1;
    while(row<=n){
        int col=1;
        int i=n-row+1;

        //print first Triangle
        while(i){
            cout<<col;
            i=i-1;
            col=col+1;
        }

        //print second Triangle
        int j=row-1;
        while(j){
            cout<<"*";
            j=j-1;
        }

        //Print Third Triangle
        int k=row-1;
        while(k){
            cout<<"*";
            k=k-1;
        }

        //print fourth Triangle
        int l=n-row+1;
        while(l){
            cout<<l;
            l=l-1;
            col=col+1;
        }
        cout<<endl;
        row=row+1;
    }
}
