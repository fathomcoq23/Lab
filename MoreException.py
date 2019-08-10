#here the __init method is not really helpful
#Hackerrank day 17


class Calculator(object):

    def power(self,a,b):
        self.a = a
        self.b = b
        if self.a>=0 and self.b >=0:
            return (a**b)
        else:
            raise Exception("n and p should be non-negative")

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   
