"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employees_dict = {e.id:e for e in employees}
        
        target_emp = employees_dict[id]
        total_importance = target_emp.importance
        
        q = target_emp.subordinates
        
        while q:
            x = q.pop(0)
            target_emp = employees_dict[x]
            
            total_importance += target_emp.importance
            if target_emp.subordinates:
                q.extend(target_emp.subordinates)
            
        return total_importance