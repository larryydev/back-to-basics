class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode('')

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.children['\0'] = '\0'
    
    def search(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return '\0' in node.children
    
    def starts_with(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True
    

if __name__ == '__main__':
    pass