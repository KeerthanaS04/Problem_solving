#include<bits/stdc++.h>
using namespace std;

void sortZeroesAndOne(int input[],int size){
    int left=0,right=size-1;
    while(left<right){
        if(input[left]!=0){
            swap(input[left],input[right--]);
        }else{
            left++;
        }
    }
}