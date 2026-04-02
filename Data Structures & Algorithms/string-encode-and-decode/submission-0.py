class Solution:

    def encode(self, strs: List[str]) -> str:
        # for each str, encode a length + # before it, (makes it so
        # when the decoder starts parsing, it will correctly work)

        # ex) 2#we3#say1#:3#yes
        finalStr = ""
        for s in strs:
            finalStr += str(len(s))
            finalStr += "#"
            finalStr += s
        return finalStr


    def decode(self, s: str) -> List[str]:
        # ex) 2#we3#say1#:3#yes
        # track an index where the parser is at, and the list of strs
        # get the length -> (parse until the # character)
        # get the substring of that length, remove it and append it 
        # to the list of words
        # update the index with length of substring
        # continue parsing
        index = 0
        strList = []

        while index < len(s):
            # start parsing for the length
            strLen = ""

            # loop while finding the int
            while s[index] != "#":
                strLen += s[index]
                index += 1
            index += 1
            intLen = int(strLen)

            # append the found string to the list
            strList.append(s[index : index + intLen])
            index += intLen
        return strList
                



    # could encode with non ascii char in between the words as breaks
    
    # encode a break character with a number tracking the length of the string
    # This lets the decoder "skip" all of the string until reading the 
    # next string, so that it doesn't matter at all what is contained
    # in the strs


