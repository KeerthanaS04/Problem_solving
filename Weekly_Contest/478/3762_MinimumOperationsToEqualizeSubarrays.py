class PersistentSegmentTree:
    class Node:
        __slots__ = ("left", "right", "cnt", "total")
        def __init__(self, left=0, right=0, cnt=0, total=0):
            self.left = left
            self.right = right
            self.cnt = cnt
            self.total = total
    
    def __init__(self, vals):
        self.sorted_unique_vals = sorted(set(vals))
        self.n = len(self.sorted_unique_vals)
        self.val_to_idx = {v:i for i, v in enumerate(self.sorted_unique_vals)}
        self.nodes = []
        self.roots = []
        self.build(vals)
    
    def new_node(self):
        self.nodes.append(self.Node())
        return len(self.nodes)-1
    
    def copy_node(self, idx):
        node = self.nodes[idx]
        self.nodes.append(self.Node(node.left, node.right, node.cnt, node.total))
        return len(self.nodes)-1
    
    def build(self, vals):
        root = self.new_node()
        self.roots.append(root)

        for x in vals:
            root = self.copy_node(root)
            self.roots.append(root)

            curr = root
            left, right = 0, self.n-1
            i = self.val_to_idx[x]

            while left<right:
                self.nodes[curr].cnt+=1
                self.nodes[curr].total+=x

                mid = (left+right)//2

                if i<=mid:
                    self.nodes[curr].left = self.copy_node(self.nodes[curr].left)
                    curr = self.nodes[curr].left
                    right = mid
                else:
                    self.nodes[curr].right = self.copy_node(self.nodes[curr].right)
                    curr = self.nodes[curr].right
                    left = mid+1
            self.nodes[curr].cnt+=1
            self.nodes[curr].total+=x
    
    def query(self, l, r):
        a = self.roots[l]
        b = self.roots[r+1]

        left_cnt = 0
        left_total = 0

        med_cnt = ((r-l+1)//2)+1
        left, right = 0, self.n-1

        while left<right:
            mid = (left+right)//2
            left_a = self.nodes[a].left
            left_b = self.nodes[b].left

            cnt = self.nodes[left_b].cnt - self.nodes[left_a].count

            if med_cnt<=cnt:
                a = left_a
                b = left_b
                right = mid
            else:
                left_cnt+=cnt
                left_total+=self.nodes[left_b].total - self.nodes[left_a].total
                med_cnt -= cnt

                a = self.nodes[a].right
                b = self.nodes[b].right
                left = mid+1
        median = self.sorted_unique_vals[left]
        total_sum = self.nodes[self.roots[r+1]].total - self.nodes[self.roots[l]].total

        return (median*left_cnt - left_total)+ \
               ((total_sum - left_total) - median*((r-l+1) - left_cnt))
    
class Solution:
    def minOperations(self, nums, k, queries):
        n = len(nums)

        # prefix check for same mod class
        prefix = [0]*(n+1)
        for i in range(n):
            if i-1>=0 and nums[i]%k!=nums[i-1]%k:
                prefix[i+1] = prefix[i]+1
            else:
                prefix[i+1] = prefix[i]
        
        vals = [x//k for x in nums]
        pst = PersistentSegmentTree(vals)

        result = []
        for s, t in queries:
            if prefix[t+1] - prefix[s+1]==0:
                result.append(pst.query(s, t))
            else:
                result.append(-1)
        return result