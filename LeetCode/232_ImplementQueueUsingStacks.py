class MyQueue:
    def __init__(self):
        self.input_st = []
        self.output_st = []
    
    def push(self, x: int) -> None:
        self.input_st.append(x)
    
    def pop(self) -> int:
        self._transfer_if_needed()
        return self.output_st.pop()
    
    def peek(self) -> int:
        self._transfer_if_needed()
        return self.output_st[-1]
    
    def empty(self) -> bool:
        return len(self.input_st)==0 and len(self.output_st)==0
    
    def _transfer_if_needed(self) -> None:
        if not self.output_st:
            while self.input_st:
                self.output_st.append(self.input_st.pop())