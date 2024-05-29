#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int equalSubstring(string s,string t,int maxCost){
        int length=s.size();
        int maxLength=0;
        int currentCost=0;
        int start=0;
        int end;

        for(end=0;end<length;end++){
            currentCost+=abs(s[end]-t[end]);

            while(currentCost>maxCost){
                currentCost-=abs(s[start]-t[start]);
                ++start;
            }
            maxLength=max(maxLength,end-start+1);
        }
        return maxLength;
    }
};