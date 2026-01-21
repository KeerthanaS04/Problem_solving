class Solution:
    def calculateSpan(self, arr):
        span, st = [], []

        for i, price in enumerate(arr):
            days = 1
            while st and arr[st[-1]]<=price:
                days+=arr[st.pop()]
            span.append(days)
            st.append(i)
        return span