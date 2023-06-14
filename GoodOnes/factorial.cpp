#include<bits/stdc++.h>
using namespace std;

int factorial(int n){
    //base case - then only our code will stop otherwise segmentation fault
    if(n==0)
       return 1;
    return n*(factorial(n-1));
}

int main(){
    int n;
    cin>>n;
    int ans=factorial(n);
    cout<<ans<<endl;

    return 0;
}