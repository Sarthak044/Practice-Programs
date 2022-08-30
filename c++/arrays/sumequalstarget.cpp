 int NumberOfMailRooms(int n, int size, vector<int>BldgX, vector<int> BldgY)
    {
        int maxN = 1e4;
        int ans;
        vector<vector<int>> graph(maxN + 1);
        vector <pair<int, int>>edges(maxN+1, {0,-1});
        vector<bool>vis(maxN+1, false);
        for (int i=0;i<size;i++){
            graph[BldgX[i]].push_back(BldgY[i]);
            graph[BldgY[i]].push_back(BldgX[i]);
            edges[BldgX[i]].first++;
            edges[BldgX[i]].second = BldgX[i];
            edges[BldgY[i]].first++;
            edges[BldgY[i]].second = BldgY[i];
        }
        sort(edges.begin(),edges.end(), greater<pair<int,int>>());
        int cnt = 0;
        for(auto deg: edges){
            int u = deg.second;
            if (u == -1){
                continue;
            }
            if (!vis[u]){
                ans++;
                vis[u] = true;
                for(int v: graph[u]){
                    if (!vis[v] && graph[v].size()<deg.first){
                        vis[v] = true;
                 }
                }
            }
         
        }
         return cnt;
       
    }