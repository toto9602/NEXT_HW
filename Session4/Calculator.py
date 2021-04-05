class Calculator: #붕어빵틀
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.result = 0

    def add(self, num1):
        self.result += num1
        return self.result #덧셈 결과값.
    
    def sub(self, num1):
        self.result -= num1
        return self.result
    
    def mul(self, num1):
        self.result *= num1
        return self.result

    def div(self, num1):
        if num1 ==0:
            return self.result
        
        self.result /= num1
        result self.result

    

calculator1 = Calculator("정상윤")
calculator1.name #정상윤

print(calculator1.add(3,5))
