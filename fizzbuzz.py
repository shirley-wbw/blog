class Fizzbuzz():
    def __init__(self,number):
        self.number=number
#    def calculate(number):
        if '7' in str(self.number):
            print('GitHub')
        elif self.number%3==0 and self.number%5==0:
            print("fizzbuzz")
        elif self.number%3==0:
            print('fizz')
        elif self.number%5==0:
            print('buzz')
        else:
            print(self.number)

#    new feature

for i in range(101):
    aaa=Fizzbuzz(i)

