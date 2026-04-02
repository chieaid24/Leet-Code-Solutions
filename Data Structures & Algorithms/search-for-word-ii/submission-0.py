class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False;

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        NUM_ROWS = len(board)
        NUM_COLS = len(board[0])
        # better than just DFS through the entire, would be implementing a Trie, addinga ll
        # words to the trie, and then stepping through each cell, and checking if it exists in our Trie
        root = TrieNode()
        # first add the words to our Trie
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            # at end of word, mark that char as the end of a word
            curr.endOfWord = True
        
        # now we have our Trie, so now apply dfs to each cell, using our Trie as our 

        # create our dfs
        # have visited set, that we add to, then call recursive, then pop so we don't need so many visited sets
        # if not valid -> return, if valid, then add to res
        res, visited = set(), set() 
        def dfs(rows: int, cols: int, node: TrieNode, word: str) -> None:
            # base cases, out of range, not equal, in seen, or end of word (valid)
            # if out of range
            if rows < 0 or rows >= NUM_ROWS or cols < 0 or cols >= NUM_COLS:
                return False
            # if in visited
            if (rows, cols) in visited:
                return False
            letter = board[rows][cols]
            if letter not in node.children:
                return False
            # go down the node, and add it to visited, and update word
            visited.add( (rows, cols) )
            node = node.children[letter]
            word += letter
            # now check if node is end of word
            if node.endOfWord:
                res.add(word)
                # you want to continue in the case that we are looking for "ba" and "back"

            # recursive call to all
            # search in all directions
            dfs(rows + 1, cols, node, word)
            dfs(rows - 1, cols, node, word)
            dfs(rows, cols + 1, node, word)
            dfs(rows, cols - 1, node, word)
            
            visited.remove( (rows, cols))
        # loop through each cell, and call DFS on it
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                dfs(row, col, root, "")
        return list(res)
            