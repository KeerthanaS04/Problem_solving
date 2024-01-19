#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int min_sprinklers(int gallery[],int n){
        vector<pair<int,int>> v;
        for(int i=0;i<n;i++){
            if(gallery[i]==-1){
                continue;
            }
            v.push_back({max(0,i-gallery[i]),min(n-1,i+gallery[i])});
        }
        sort(v.begin(),v.end());
        int start=0,i=0,count=0;
        while(start<n){
            int maxa=INT_MIN;
            while(i<v.size()){
                if(v[i].first>start)
                    break;
                maxa=max(maxa,v[i].second);
                i++;
            }
            if(maxa<start){
                return -1;
            }
            count++;
            start=maxa+1;
        }
        return count;
    }
};
