#include<bits/stdc++.h>
#include<vector>
using namespace std;

class Solution{
    private:
        bool valid(char ch){
            if((ch>'a' && ch<'z') || (ch>'A' && ch<'Z') || (ch>'0' && ch<'9')){
                return 1;
            }else{
                return 0;
            }
        }
        char toLowerCase(char ch){
            if((ch>='a' && ch<='z')||(ch>='0' && ch<='9')){
                return ch;
            }else{
                char temp=ch-'A'+'a';
                return temp;
            }
        }
        bool checkPalindrome(string a){
            int start=0;
            int end=a.length()-1;

            while(start<=end){
                if(a[start]!=a[end]){
                    return 0;
                }else{
                    start++;
                    end--;
                }
            }
            return 1;
        }
    public:
        bool isPalindrome(string s){
            string temp="";
            for(int i=0;i<s.length();i++){
                if(valid(s[i])){
                    temp.push_back(s[i]);
                }
            }
            //make everything lowercase
            for(int i=0;i<temp.length();i++){
                temp[i]=toLowerCase(temp[i]);
            }
            return checkPalindrome(temp);
        }
};