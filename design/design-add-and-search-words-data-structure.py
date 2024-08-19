class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        
        # if the char is "." recurse on the children 
        ## else if: the char not match, return False
        ### recursive steps: if the previous char matches => continue to the next char in the 
        #### word 
        ##### => don't need to check "."
        def dfs(j, root): #j: index word[j] ; root: current Trie Node
            cur = root

            for i in range(j, len(word)): #iterate through all the chracters in the word
                if word[i] == ".":
                    # try all possible chars in the children list -> compare the next character 
                    ## and all the nodes in the children list
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    #if all choice tried and not found a matching one
                    return False
                else:
                    if word[i] not in cur.children:
                        return False
                    cur = cur.children[word[i]]
            return cur.word
        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)