class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # basically loop through each word in pairs, and check if they are valid
        # makes it easier if we create a dict of the char: index in the order, so we can
        # check in O(1) time whether two chars are valid or not
        orderInd = {c:i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for c in range(len(w1)):
                if c == len(w2):
                    return False
                
                if w1[c] != w2[c]:
                    # different letters, so now compare once
                    if orderInd[w1[c]] > orderInd[w2[c]]:
                        return False
                    break
        return True
            