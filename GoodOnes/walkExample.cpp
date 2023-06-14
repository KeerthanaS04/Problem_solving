#include<bits/stdc++.h>
using namespace std;

void reachHome(int src,int dest){
    //base case
    cout<<"Source "<<src<<endl;
    if(src==dest){
        cout<<"Reached"<<endl;
        return ;
    }

    //processing - one step more
    src++;

    //recursive call
    reachHome(src,dest);
}

int main(){
    int dest=10;
    int src=1;

    cout<<endl;
    reachHome(src,dest);

    return 0;
}