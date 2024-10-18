from typing import List
import heapq

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_set = set(positive_feedback)
        negative_set = set(negative_feedback)
        
        scores = {}
        
        for i, feedback in enumerate(report):
            words = feedback.split()
            student = student_id[i]
            score = 0
            
            for word in words:
                if word in positive_set:
                    score += 3
                elif word in negative_set:
                    score -= 1
            
            scores[student] = scores.get(student, 0) + score
        
        heap = []
        
        for student, score in scores.items():
            heapq.heappush(heap, (-score, student))
        
        top_k_students = []
        
        for _ in range(k):
            top_k_students.append(heapq.heappop(heap)[1])
        
        return top_k_students