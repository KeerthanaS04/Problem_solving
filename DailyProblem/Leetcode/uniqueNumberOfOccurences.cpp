#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    bool uniqueOccurences(vector<int>& arr){
        vector<int> ans;
        sort(arr.begin(),arr.end());
        for(int i=0;i<arr.size();){
            int count=1;
            for(int j=i+1;j<arr.size();j++){
                if(arr[i]==arr[j]){
                    count++;
                }
            }
            ans.push_back(count);
            i+=count;
        }

        sort(ans.begin(),ans.end());
        for(int i=0;i<ans.size()-1;i++){
            if(ans[i]==ans[i+1]){
                return false;
            }
        }
        return true;
    }
};
