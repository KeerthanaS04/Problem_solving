class Solution:
    def pythagoreanTriplet(self, arr):
        st = set()

        for a in arr:
            st.add(a*a)
        
        for a in st:
            for b in st:
                if a!=b:
                    if (a+b) in st:
                        return True
        return False