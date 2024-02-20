class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(strs):
        return ' '.join(strs)

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(str):
        strs = list()
        temp = ""
        for i in str:
        # could also use i == " "
            if i.isspace():
                strs.append(temp)
                temp = ""
            else:
                temp += i
        strs.append(temp)
        return strs

strs = ["we", "say", ":", "yes"]
encoded = Solution.encode(strs)
decoded = Solution.decode(encoded)
print("Encoded string from list: ", encoded, 
      "\nDecoded list from string: ", decoded)