class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(char_index: int) -> int:
            if parent[char_index]!=char_index:
                parent[char_index] = find(parent[char_index])
            return parent[char_index]
        parent = list(range(26))
        for char1, char2 in zip(s1, s2):
            index1 = ord(char1)-ord('a')
            index2 = ord(char2)-ord('a')

            root1 = find(index1)
            root2 = find(index2)

            if root1<root2:
                parent[root2] = root1
            else:
                parent[root1] = root2
        result = []
        for char in baseStr:
            char_index = ord(char)-ord('a')
            smallest_index = find(char_index)
            result.append(chr(smallest_index+ord('a')))
        return ''.join(result)