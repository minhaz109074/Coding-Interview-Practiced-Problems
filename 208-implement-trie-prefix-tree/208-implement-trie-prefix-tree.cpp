class TrieNode {
public:
    TrieNode* children[26] = {};
    bool is_word = false;
    TrieNode* get(char c) { return children[c - 'a'];}
    void add(char c) { children[c - 'a'] = new TrieNode();}
    
};

class Trie {
    TrieNode* root = new TrieNode();
public:
    Trie() {
        
    }
    
    void insert(string word) {
        auto node = root;
        for(auto& c: word){
            if (!node->get(c)){
                node->add(c);
            }
            node = node->get(c);
        }
        node->is_word = true;
        
    }
    
    bool search(string word) {
        auto node = root;
        for(auto& c: word){
            if (!node->get(c)){
               return false;
            }
            node = node->get(c);
        }
        return node->is_word;
        
    }
    
    bool startsWith(string prefix) {
        auto node = root;
        for(auto& c: prefix){
            if (!node->get(c)){
               return false;
            }
            node = node->get(c);
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */