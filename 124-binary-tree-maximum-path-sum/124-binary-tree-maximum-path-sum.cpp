/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    int maxSide(TreeNode* root, int& ans){
        if (!root) return 0;
        
        int left = maxSide(root->left, ans);
        int right = maxSide(root->right, ans);
        int maxside = max(root->val, max(left, right) + root->val);
        int maxtop = max(maxside, left+right+root->val);
        ans = max(ans, maxtop);
        return maxside;
        
    }
public:
    int maxPathSum(TreeNode* root) {
        int ans = INT_MIN;
        maxSide(root, ans);
        return ans;
            
        
    }
};