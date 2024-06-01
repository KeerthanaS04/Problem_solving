#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int swapNibbles(int n){
        return (n&0x0F)<<4 | (n>>4);
    }
};