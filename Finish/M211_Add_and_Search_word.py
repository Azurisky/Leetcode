class WordDictionary(object):

    ## Use trie
    class TrieNode:
        # Initialize your data structure here.
        def __init__(self):
            self.children = {}
            self.is_word = False

    class WordDictionary(object):

        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.root = TrieNode()

        def addWord(self, word):
            """
            Adds a word into the data structure.
            :type word: str
            :rtype: void
            """
            node = self.root
            for i in word:
                node.children[i] = node.children.get(i, TrieNode())
                node = node.children[i]
            node.is_word = True
        
        
        def search(self, word):        
            def find(node, word):
                if not word:
                    return node.is_word
                ch = word[0]
                word = word[1:]
                if ch != '.' and ch not in node.children:
                    return False
                elif ch in node.children:
                    node = node.children[ch]
                    return find(node, word) 
                elif ch == '.':
                    tmp = False
                    for i in node.children:
                        tmp = tmp or find(node.children[i], word)
                    return tmp 
            return find(self.root, word)

    ## Use len to be faster
    def __init__(self):
        self.l = {}

    def addWord(self, word):
        self.l[len(word)] = self.l.get(len(word), [])
        self.l[len(word)].append(word)

    def search(self, word):
        if not word:
            return False
        
        self.l[len(word)] = self.l.get(len(word), [])
        
        if '.' not in word:
            return word in self.l[len(word)]

        for v in self.l[len(word)]:
            count = 0
            for i, c in enumerate(word):
                if c != '.' and v[i] != c:
                    break
                count += 1
            if count == len(word):
                return True
        return False
    
    ## TLE
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bank = {}
        
    def fillBank(self, word):
        if word not in self.bank:
            self.bank[word] = 1

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.fillBank(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if '.' not in word:
            if word in self.bank:
                return True
        for j in self.bank:
            if len(j) == len(word):
                count = 0
                for i, c in enumerate(word):
                    if c != '.' and c != j[i]:
                        break
                    else:
                        count += 1
                if count == len(word):
                    return True
        return False