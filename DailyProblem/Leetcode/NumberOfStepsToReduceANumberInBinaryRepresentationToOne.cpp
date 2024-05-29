#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int numSteps(string s){
        int steps=0;
        bool carry=false;
        for(int i=s.size()-1;i>0;i--){
            char bit=s[i];

            //If there's carry from the previous operation
            if(carry){
                //Find the current bit due to the carry
                if(bit=='0'){
                    bit='1';
                    carry=false; //The carry has been used, reset it to false
                }else
                    bit='0' //If the bit is '1', turning into '0' keeps carry true
            }

            //If the bit is '1', we will need a step it to make it '0' and create carry
            if(bit=='1'){
                steps++;
                carry=true;
            }
            //regardless of bit, we make a right-shift operator
            steps++;
        }
        //If there's a carry at the end, we need to add one more step to add it to the MSB
        if(carry) steps++;

        return steps;
    }
};