class MountainArray:
    def get(self, index: int) -> int:
    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def search_ascending(l: int, r: int) -> int:
            first_true_idx = -1
            while l<=r:
                mid = (l+r)//2
                if mountainArr.get(mid)>=target:
                    first_true_idx = mid
                    r = mid-1
                else:
                    l = mid+1
            
            if first_true_idx!=-1 and mountainArr.get(first_true_idx)==target:
                return first_true_idx
            return -1
        
        def search_descending(l: int, r: int) -> int:
            first_true_idx = -1
            while l<=r:
                mid = (l+r)//2
                if mountainArr.get(mid)<=target:
                    first_true_idx = mid
                    r = mid-1
                else:
                    l = mid+1
            
            if first_true_idx!=-1 and mountainArr.get(first_true_idx)==target:
                return first_true_idx
            return -1
        
        n = mountainArr.length()
        # find peak element using binary search template on descending array
        l, r = 0, n-1
        first_true_idx = -1
        while l<=r:
            mid = (l+r)//2
            if mid<n-1 and mountainArr.get(mid)>mountainArr.get(mid+1):
                first_true_idx = mid
                r = mid-1
            else:
                l = mid+1
        peak_idx = first_true_idx

        # search in ascending part
        res = search_ascending(0, peak_idx)
        # if not found, search in descending part
        if res==-1:
            res = search_descending(peak_idx+1, n-1)
        return res