class Solution:
    def exitPoint(self, mat):
        n, m = len(mat), len(mat[0])
        i, j = 0,0
        previ, prevj = 0,0
        face = 0 # 0=right, 1=down, 2=left, 3=up

        while 0<=i<n and 0<=j<m:
            previ, prevj = i, j

            if mat[i][j] == 1:
                mat[i][j] = 0

                if face == 0:
                    i += 1
                    face = 1
                elif face == 1:
                    j -= 1
                    face = 2
                elif face == 2:
                    i -= 1
                    face = 3
                else:
                    j += 1
                    face = 0
            else:
                if face == 0:
                    j += 1
                elif face == 1:
                    i += 1
                elif face == 2:
                    j -= 1
                else:
                    i -= 1
        return [previ, prevj]