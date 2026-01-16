from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculateSalary(self):
        pass

class Intern(Employee):
    def __init__(self, hourlyRate, totalWorkHours):
        self.hourlyRate = hourlyRate
        self.totalWorkHours = totalWorkHours
    def calculateSalary(self):
        return self.hourlyRate * self.totalWorkHours
    
class FullTimeEmployee(Employee):
    def __init__(self, base, bonus, deductions):
        self.base = base
        self.bonus = bonus
        self.deductions = deductions
    def calculateSalary(self):
        return self.base + self.bonus - self.deductions
    
class ContractEmployee(Employee):
    def __init__(self, contractSalary):
        self.contractSalary = contractSalary
    def calculateSalary(self):
        return self.contractSalary
    
fte = FullTimeEmployee(base=70_000, bonus=15000, deductions=20000)
intern = Intern(hourlyRate=100, totalWorkHours=60)
contractor = ContractEmployee(contractSalary=65000)

print(f"Salary of Full-Time-Employee = Rs.{fte.calculateSalary()}\nSalary of Intern = Rs.{intern.calculateSalary()}\nSalary of Contractor = Rs.{contractor.calculateSalary()}")