#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;

    int row=1;
    while(row<=n){
        //Print space(first triangle)
        int space=n-row;
        while(space){
            cout<<" ";
            space=space-1;
        }
        
        //Print second triangle
        int j=1;
        while(j<=row){
            cout<<j;
            j=j+1;
        }

        //Print third triangle
        int start=row-1;
        while(start){
            cout<<start;
            start=start-1;
        }

        cout<<endl;
        row=row+1;
    }
}