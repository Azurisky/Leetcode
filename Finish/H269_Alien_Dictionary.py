class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        pre, suc = collections.defaultdict(set), collections.defaultdict(set)
        for x, y in zip(words, words[1:]):
            for a, b in zip(x, y):
                if a != b:
                    suc[a].add(b)
                    pre[b].add(a)
                    break
        # print(pre)
        # print(suc)
        chars = set(''.join(words))
        free = chars - set(pre)
        # print(free)
        order = ''
        while free:
            a = free.pop()
            order += a
            for b in suc[a]:
                pre[b].discard(a)
                if not pre[b]:
                    free.add(b)
        return order * (set(order) == chars)