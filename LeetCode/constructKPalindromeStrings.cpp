#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    bool canConstruct(string s,int k){
        if(s.size()<k) return false;
        map<int,int> m;
        int no=0;
        for(a:s)m[a]++; //store the counting of each letter in the map
        for(a:m)if(a.second%2==1)no++; //counting increasing for odd numbers of letters
        return no<=k;
    }
};