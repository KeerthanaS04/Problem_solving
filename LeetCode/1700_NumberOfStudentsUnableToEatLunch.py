from typing import List
from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_preferences = Counter(students)

        for sandwich_type in sandwiches:
            if student_preferences[sandwich_type]==0:
                # return the count of students wanting the other type
                return student_preferences[sandwich_type^1]
            student_preferences[sandwich_type]-=1
        return 0