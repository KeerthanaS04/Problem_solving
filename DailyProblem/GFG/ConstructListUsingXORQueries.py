class Solution:
    def constructList(self, queries):
        x = 0
        ans = []

        for i in range(len(queries)-1, -1, -1):
            if queries[i][0]:
                x^=queries[i][1]
            else:
                ans.append(queries[i][1]^x)
        ans.append(x)
        ans.sort()
        return ans