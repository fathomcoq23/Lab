class Difference:
    def __init__(self, a):
        self.__elements = a
   
	# Add your code here
    def computeDifference(self):
        self.maximumDifference = None
        for i, d in enumerate(self.__elements):
            for g, l in enumerate(self.__elements):
                if i != g:
                    result = abs(self.__elements[g] - self.__elements[i])
                    if self.maximumDifference is None:
                        self.maximumDifference = result
                    else:
                        if self.maximumDifference < result:
                            self.maximumDifference = result

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
