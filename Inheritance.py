class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    def __init__(self,firstName,lastName,IdNumber,scores):
        super().__init__(firstName, lastName,IdNumber)
    #   Parameters:
        self.count = 0
        self.score = scores
        for i in self.score:
            self.count += 1

    def calculate(self):
        self.total = sum(self.score)
        self.average = self.total// self.count

        if self.average <= 100 and self.average >=90:
            return ("O")
        elif self.average >= 80 and self.average < 90:
            return ("E")
        elif self.average >= 70 and self.average < 80:
            return ("A")
        elif self.average >= 55 and self.average < 70:
            return ("P")
        elif self.average >= 40 and self.average < 55:
            return ("D")
        else:
            return ("T")

line = input().split()
