class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        ## BFS
        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    d[s] = d.get(s, []) + [word]
            return d
            
        def bfs_words(begin, end, dict_words):
            queue = [(begin, 1)]
            visited = set()
            while queue:
                word, steps = queue.pop(0)
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i+1:]
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
            return 0
        
        d = construct_dict(wordList)
        return bfs_words(beginWord, endWord, d)


        ## Pass, use map to be faster
        word_list = wordList
        l = len(endWord)
        if endWord not in word_list: 
            return 0

        # group words that differ in i-th position
        i_differ_list = []
        for i in range(l):
            i_differ_map = {}
            for word in word_list:
                substr = word[:i]+word[i+1:]
                if substr not in i_differ_map:
                    i_differ_map[substr] = []
                i_differ_map[substr].append(word)
            i_differ_list.append(i_differ_map)
            
        queue = [(1, beginWord)]
        visited = set()
        visited.add(beginWord)
        while queue:
            depth, word = queue.pop(0)
            # find all words that differ in i-th position
            # from the current word
            for i in range(word_len):
                substr = word[:i]+word[i+1:]
                for next_word in i_differ_list[i].get(substr, []):
                    if next_word == endWord: 
                        return depth+1
                    if next_word not in visited:
                        visited.add(next_word)
                        queue.append((depth+1, next_word))
                        
        # the end_word is in the list
        # but there is no path to it
        return 0

        ## TLE
        ans = 1
        if endWord not in wordList:
            return 0
        
        if beginWord not in wordList:
            wordList.append(beginWord)
        visit = {}
        visit[endWord] = 1
        stack = [endWord]
        tmp = []
        while stack:        
            w = stack.pop()
            for i in wordList:
                c = 0
                for l in range(len(i)):
                    if i[l] != w[l]:
                        c += 1
                if c == 1 and i not in visit:
                    tmp.append(i)
                    visit[i] = 1
                    
            for i in tmp:
                if i == beginWord:
                    return ans + 1
                    
            if not stack:
                ans += 1
                # print(tmp, ans)
                stack = tmp
                tmp = []
        return 0