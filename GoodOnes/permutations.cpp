#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    // Such a solution will exist for all n, except 2 and 3
    if(n == 2 || n == 3){
        cout<<"No Solution"<<endl;
    }else{
        for(int i = 1; i <= n; i += 2){
            cout<<i<<' ';
        }
        for(int i = 2; i <= n; i += 2){
            cout<<i<<' ';
        }
    }
    return 0;
}