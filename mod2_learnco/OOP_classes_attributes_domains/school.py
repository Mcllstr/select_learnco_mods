class School():
    def __init__(self, name = None, roster = {}):
        self.name = name
        self.roster = roster
    
    def add_student(self, newname, grade):
        if grade in list(self.roster.keys()):
            self.roster[grade].append(newname)
        else:
            self.roster[grade] = [newname]
    
    def grade(self, grade):
        return self.roster[grade]
    
    def reset_roster(self):
        self.roster = {}
    
    def sort_roster(self):
        
        for key in self.roster:
            self.roster[key].sort()
        return self.roster
        
        
        
#         new_dict = self.roster
#         for key in new_dict:
#             new_dict[key].sort()
#         return new_dict
        
      
    #     for entry in self.roster:
#             print(self.roster[entry])
#             #self.roster[entry] = self.roster[entry].sort()
#             print(self.roster[entry].sort())
#         return new_dict