class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        
        ## Union Find
        def find(a):
            if ds[a] < 0:
                return a
            ds[a] = find(ds[a])
            return ds[a]
        
        def union(a, b):
            a, b = find(a), find(b)
            if a != b:
                if ds[a] < ds[b]:
                    ds[a] += ds[b]
                    ds[b] = a
                else:
                    ds[b] += ds[a]
                    ds[a] = b

        c, ds, email_to_id, id_to_name = 0, [], {}, {}
        for account in accounts:
            for email in account[1:]:
                if email not in email_to_id:
                    email_to_id[email] = c
                    id_to_name[c] = account[0]
                    ds.append(-1)
                    c += 1
                union(email_to_id[account[1]], email_to_id[email])        
                
        res = {}
        for email, id in email_to_id.items():
            master = find(id)
            res[master] = res.get(master, []) + [email]
        return [[id_to_name[id]] + sorted(emails) for id, emails in res.items()]
        
        ## dfs        
        from collections import defaultdict
        def accountsMerge(self, accounts):
        emails_to_idx = {}
        edges = defaultdict(list)
        for i, a in enumerate(accounts):
            for email in a[1:]:
                if email in emails_to_idx:
                    j = emails_to_idx[email]
                    edges[i].append(j)
                    edges[j].append(i)
                else:
                    emails_to_idx[email] = i
        visited = set()

        def dfs(i, s):
            if i not in visited:
                s.update(accounts[i][1:])
                visited.add(i)
                for j in edges[i]:
                    dfs(j, s)

        r = []
        for i in range(len(accounts)):
            if i not in visited:
                s = set()
                dfs(i, s)
                r.append([accounts[i][0]] + list(sorted(s)))
        return r