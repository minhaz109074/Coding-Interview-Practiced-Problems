class TimeMap {
public:
    unordered_map<string, vector<pair<int, string>>> mp;
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        mp[key].push_back({timestamp, value});
    }
    
    string get(string key, int timestamp) {
        if (mp.find(key) == mp.end()) {
            return "";
        }
        int l = 0, r = mp[key].size();
        while(l<r){
            int mid = (l+r) >> 1;
            if (timestamp < mp[key][mid].first){
                r = mid;
            }
            else {
                l = mid + 1;
            }
                
        }
        return l > 0 and l<=mp[key].size() ? mp[key][l-1].second : "";
            
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */