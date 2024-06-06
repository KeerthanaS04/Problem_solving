#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    vector<string> commonChars(vector<string>& words){
        int letterCount[26];
        memset(letterCount,0x3f,sizeof(letterCount));

        //Loop through each word in the words vector
        for(const auto& word:words){
            //Local count for letters in the current word
            int wordLetterCount[26]={0};

            //count each letter in the current word
            for(char letter:word){
                ++wordLetterCount[letter-'a'];
            }

            //compare counts for each letter with the global count and take the minimum
            for(int i=0;i<26;i++){
                letterCount[i]=min(letterCount[i],wordLetterCount[i]);
            }
        }
        //prepare the result vector to store common letters
        vector<string> result;
        for(int i=0;i<26;i++){
            //Add the appropriate number of the current letter to the result
            while(letterCount[i]>0){
                result.emplace_back(1,static_cast<char>(i+'a'));
                --letterCount[i];
            }
        }
        return result;
    }
};