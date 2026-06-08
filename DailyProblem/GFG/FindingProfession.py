class Solution:
    def profession(self, level, pos):
        is_opposite = False

        while pos!=1:
            if pos%2==0:
                is_opposite=not is_opposite
            pos = (pos+1)//2
        return 'Doctor' if is_opposite else 'Engineer'