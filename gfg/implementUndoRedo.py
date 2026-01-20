class Solution:
    def __init__(self):
        self.str = ""
        self.v = []
    
    def append(self, x):
        self.str+=x
    
    def undo(self):
        if not self.str:
            return
        self.v.append(self.str[-1])
        self.str = self.str[:-1]
    
    def redo(self):
        if not self.v:
            return
        self.str+=self.v.pop()
    
    def read(self):
        return self.str