class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = [i for i in range(n)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        count = n   
        for u,v in edges:
            pu = find(u)
            pv = find(v)

            if pu != pv:
                count -= 1         
                parent[pu] = pv
        return count         

        