amount = 0


class Counter :



    def __init__(self) :

        self.amount = 0



    def incremen(self) :

        self.amount = self.amount + 1
        
        return self.amount

    def decrements(self) :

        self.amount = self.amount + 1

        return self.amount

    def reset(self) :

        self.amount = 0

        return self.amount


number = Counter()

print(number.incremen())


print(number.incremen())

        