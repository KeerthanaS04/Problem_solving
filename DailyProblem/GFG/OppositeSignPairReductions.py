class Solution:
    def reducePairs(self, arr):
        stack = []

        for x in arr:
            stack.append(x)

            while len(stack):
                top = stack[-1]
                second = stack[-2]

                if top*second<0:
                    stack.pop()
                    stack.pop()

                    if abs(top)==abs(second):
                        continue
                    elif abs(top)>abs(second):
                        stack.append(top)
                    else:
                        stack.append(second)
                else:
                    break
        return stack