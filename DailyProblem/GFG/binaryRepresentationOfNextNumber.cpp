#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    string binaryNextNumber(string s){
        bool indication=true;
        for(int i=s.length();i>=0;i--){
            if(s[i]=='0'){
                s[i]='1';
                indication=false;
                break;
            }else{
                s[i]='0';
            }
        }
        if(indication){
            s='1'+s;
        }else{
            while(s[0]=='0') s.erase(s.begin());
        }
        return s;
    }
};