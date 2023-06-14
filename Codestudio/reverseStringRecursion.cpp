#include <bits/stdc++.h> 
void reverse(string& str,int i,int j){
    // cout<<"Call receieved for "<<str<<endl;
    //base case
    if(i>j)
      return;
    swap(str[i],str[j]);
    i++;
    j--;

    //Recursive call
    reverse(str,i,j);
}

string reverseString(string str)
{
	reverse(str,0,str.length()-1);
	return str;
}