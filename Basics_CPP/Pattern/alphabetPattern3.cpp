#include<bits/stdc++.h>
using namespace std;

int main(){
    int n=1;
    cin>>n;

    /*
    i+j-1 = 1
    => i+j-1+'A'-1 = 'A'-1+1
    => 'A'+i+j-2 = 'A'
    */

    int row=1;
    while(row<=n){
        int col=1;
        while(col<=n){
            char ch='A'+row+col-2;
            cout<<ch;
            col=col+1;
        }
        cout<<endl;
        row=row+1;
    }
}