#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    vector<int> singleNumber(vector<int>& nums){
        //initial total XOR value for all numbers in the array
        long long int total_xor=0;
        for(int num:nums){
            total_xor^=num;
        }
        //find the rightmost set bit in the total XOR (first bit that differs between two unique n)
        int last_bit=total_xor&(-total_xor);
        int num1=0;
        for(int num:nums){
            //separate numbers into two groups and find the first unique number by XORing numbers in t
            if(num&last_bit){
                num1^=num;
            }
        }
        //the second unique number is found by XORing the first number with the initial total_XOR
        int num2=total_xor^num1;

        return {num1,num2};
    }
};