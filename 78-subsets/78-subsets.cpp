class Solution {
    
    void dfs(vector<int>& nums, vector<vector<int>>& ans, vector<int>& subset, int index){
        if (index == nums.size()){
            ans.push_back(subset);
            return;
        }
        
        subset.push_back(nums[index]);
        dfs(nums, ans, subset, index+1);
        
        subset.pop_back();
        dfs(nums, ans, subset, index+1);
            
    }
    
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> subset;
        dfs(nums, ans, subset, 0);
        return ans;
        
    }
};