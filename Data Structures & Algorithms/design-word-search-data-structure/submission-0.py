class TrieNode:
    def __init__(self):
        self.children = {} # (str: TrieNode)
        self.endOfWord = False

class WordDictionary:
    # can implement a Trie, for any ., it would result in a DFS in finding the last part thorugh
    # all possibilites
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                # create a new node
                curr.children[char] = TrieNode()
                print("appended: ", char, curr.children[char])
            curr = curr.children[char]
        print("End of word")
        curr.endOfWord = True
            

    def search(self, word: str) -> bool:
        def dfs(node, substr) -> bool:
            # check base cases
            if not substr:
                if node.endOfWord == True:
                    return True
                else:
                    return False
            # recursive step
            char = substr[0]
            # deal with .
            if char == ".":
                # special logic
                # go down EVERY child, passing substr[1:], if any child is valid, return True
                flag = False
                print(node.children)
                for child, childNode in node.children.items():
                    if dfs(node.children[child], substr[1:]):
                        flag = True
                return flag
            elif char in node.children:
                # go down this path 
                return dfs(node.children[char], substr[1:])
            else:
                return False

        return dfs(self.root, word)
        

            


                
