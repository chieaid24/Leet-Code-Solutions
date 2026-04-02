class TreeNode:
    def __init__(self):
        self.endOfWord = False
        self.children = {} #char: TreeNode

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TreeNode()
            curr = curr.children[c]
        # at the end of word, add the flag
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            # check if the character is present
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            # check if the character is present
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        