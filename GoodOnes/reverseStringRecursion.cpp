#include<bits/stdc++.h>
using namespace std;

void reverse(string& str,int i,int j){
    cout<<"Call receieved for "<<str<<endl;
    //base case
    if(i>j)
      return;
    swap(str[i],str[j]);
    i++;
    j--;
    
    //Recursive call
    reverse(str,i,j);
}

int main(){
    string name="KeerthanaS";
    cout<<endl;
    reverse(name,0,name.length()-1);
    cout<<endl;
    cout<<name<<endl;

    return 0;
}