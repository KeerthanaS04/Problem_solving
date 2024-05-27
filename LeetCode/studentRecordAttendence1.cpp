#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    bool checkRecord(string s){
        bool isAbsenceLessThanTwo=count(s.begin(),s.end(),'A')<2;
        bool consecutiveLates=s.find("LLL")===string::npos;
        //The s is ineligible if 'LLL' is found

        return isAbsenceLessThanTwo && consecutiveLates;
    }
};