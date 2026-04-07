from collections import deque
class Solution:
    def stableMarriage(self, men, women):
        n = len(men)
        womanPartner = [-1]*n
        manPartner = [-1]*n
        nextProposal = [0]*n

        # ranking matrix for women
        ranks = [[-1]*n for _ in range(n)]
        for w in range(n):
            for rank in range(n):
                ranks[w][women[w][rank]] = rank
        freemen = deque(range(n))

        while freemen:
            man = freemen.popleft()
            woman = men[man][nextProposal[man]]
            nextProposal[man]+=1

            if womanPartner[woman]==-1:
                womanPartner[woman] = man
                manPartner[man] = woman
            else:
                curr_man = womanPartner[woman]

                if ranks[woman][man]<ranks[woman][curr_man]:
                    womanPartner[woman] = man
                    manPartner[man] = woman

                    freemen.append(curr_man)
                    manPartner[curr_man]-=1
                else:
                    freemen.append(man)
        return manPartner