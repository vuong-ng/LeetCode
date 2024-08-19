class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        #2 hash maps
        """
        w_p = {}
        wlist = s.split(' ')
        p_w = {}
        if len(pattern) != len(wlist):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in p_w:
                p_w[pattern[i]] = wlist[i]
            if wlist[i] not in w_p:
                w_p[wlist[i]] = pattern[i]
            if  wlist[i] != p_w[pattern[i]] or pattern[i] != w_p[wlist[i]]: 
                return False
        return True
        """
        #single index hash map
        wlist = s.split(' ')
        single_ind = {}
        if len(pattern) != len(wlist):
            return False
        for i in range(len(pattern)):
            char_key = 'char_{}'.format(pattern[i])
            char_word = 'word_{}'.format(wlist[i])
            if char_key not in single_ind: 
                single_ind[char_key] = i
            if char_word not in single_ind:
                single_ind[char_word] = i
            
            if single_ind[char_key] != single_ind[char_word]:
                return False
        return True
            
