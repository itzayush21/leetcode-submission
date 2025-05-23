"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        emap={e.id:e for e in employees}
        def dfs(n):
            imp=emap[n].importance
            for s in emap[n].subordinates:
                imp+=dfs(s)

            return imp
        return dfs(id)
        