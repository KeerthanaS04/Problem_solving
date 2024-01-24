/*
0 ->1 ->3
 _\|  -/|
    2
Here indegree for numbers=>  0->0
(those which are receieving) 1->1
                             2->1
                             3->2
In queue, it contains those which have indegree 0. It cuts each indegrees by one and add in the queue, and then pop up                             
*/

#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    vector<int> findOrder(int n,int m,vector<vector<int>> prerequisites){
        vector<int> adj[n];
        for(auto it:prerequisites){
            adj[it[1]].push_back(it[0]);
        }
        vector<int> indegree(n,0);
        for(int i=0;i<n;i++){
            for(auto it:adj[i]){
                indegree[it]++;
            }
        }
        queue<int> q;
        for(int i=0;i<n;i++){
            if(indegree[i]==0){
                q.push(i);
            }
        }
        vector<int> topo;
        while(!q.empty()){
            int node=q.front();
            q.pop();
            topo.push_back(node);
            //node is in your topo sort, so please remove it from the indegree
            for(auto it:adj[node]){
                indegree[it]--;
                if(indegree[it]==0) q.push(it);
            }
        }
        if(topo.size()==n) return topo;
        return {};
    }
};