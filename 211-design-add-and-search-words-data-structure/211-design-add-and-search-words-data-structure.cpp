class TrieNode{
public:
    TrieNode* children[26] = {};
    bool is_word = false;
    TrieNode* get(char c) { return children[c - 'a'];}
    void add(char c) { children[c - 'a'] = new TrieNode();}
};

class WordDictionary {
    TrieNode* root = new TrieNode();
public:
    WordDictionary() {
        
    }
    
    void addWord(string word) {
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
        
        return dfsSearch(word, 0, root);
    }
    
private:
    bool dfsSearch(string &word, int pos, TrieNode* node){
        if (!node){ return false;}
        if (pos == word.size()) { return node->is_word;}

        if (word[pos] != '.'){
            node = node->get(word[pos]);
            return dfsSearch(word, pos+1, node);
        }
        
        for(auto c = 0; c < 26; c++){
            if (dfsSearch(word, pos+1, node->children[c])) return true;
        }
        return false;
        
    }
};


/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */