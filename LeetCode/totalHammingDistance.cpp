#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int totalHammingDistance(vector<int>& nums){
        int totalDistance=0; //initiating total Hamming Distance=0

        //Loop over each bit position(32 bits)
        for(int bitPosition=0;bitPosition<31;bitPosition++){
            int countOnes=0; //number of elements with the current bit set to 1
            int countZeros=0; //number of elements with the current bit set to 0

            //Iterate over all the numbers in the array
            for(int num:nums){
                //Isolate the bit at the current position 'bitPosition'
                int bitValue=(num>>bitPosition)&1;

                if(bitValue==1){
                    countOnes++;
                }else{
                    countZeros++;
                }
            }
            totalDistance+=countOnes*countZeros;
        }
        return totalDistance;
    }
};