class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        res = []
        i=0
        while s != '':
            if s[i] =='#':
                n = int(s[:i])
                res.append(s[i+1:i+1+n])
                s = s[i+1+n:]
                i=0
            else:
                i+=1
        return res
            



         

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))