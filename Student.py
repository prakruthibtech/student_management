# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 12:31:54 2024

@author: microsoft
"""

class S:
    def __init__(self,USN,Name,Branch,Sem,Marks):
        self.USN=USN
        self.Name=Name
        self.Branch=Branch
        self.Sem=Sem
        self.Marks=Marks
    def calGrade(self,Marks):
        if self.Marks>=90 and self.Marks<=100:
            return "A+"
        elif self.Marks>=80:
            return "A"
        elif self.Marks>=70:
            return "B"
        elif self.Marks>=60:
            return "C"
        elif self.Marks>=50:
            return "D"
        elif self.Marks<=50:
            return "FAIL"
    def __str__(self):
         return self.USN
S1=S("URCSE001","RAJA","CSE",1,90)
print(S1)     