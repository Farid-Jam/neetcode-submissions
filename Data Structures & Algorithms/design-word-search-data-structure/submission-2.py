class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.endOfWord
            
            if word[i] != '.' and word[i] not in node.children:
                return False
            
            if word[i] in node.children:
                return dfs(node.children[word[i]], i + 1)
            
            if word[i] == '.':
                for c in node.children:
                    if dfs(node.children[c], i + 1):
                        return True
            
            return False
        
        return dfs(self.root, 0)