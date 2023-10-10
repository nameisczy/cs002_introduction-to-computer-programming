class Gumball_Machine:
    def __init__(self, capacity):
        self.money = 0
        self.color = []
        import random
        for i in range(capacity):
            rando = random.randint(0,2)
            if rando == 0:
                self.color = self.color + ['red']
            elif rando == 1:
                self.color = self.color + ['green']
            elif rando == 2:
                self.color = self.color + ['blue']
        print("Gumball Machine created with", capacity, "random gumballs")
        print()

    def report(self):
        print("Gumball Machine Report:")
        print("* Gumballs in machine:", len(self.color))
        print("* Money in machine: $" + format(self.money, '.2f'))
        print()

    def dispense(self, coin):
        if len(self.color) > 0:
            if coin == 0.25:
                import random
                rand = random.randint(0,len(self.color) - 1)
                po = self.color.pop(rand)
                print("Accepting 0.25; Dispensing a", po, "gumball")
                self.money = self.money + 0.25
            else:
                print("Invalid coin, no gumball will be dispensed")
        else:
            print("Machine is empty, no gumball will be dispensed")
        print()

    def count_gumballs_by_type(self, type_):
        if type_ == 'red':
            print("There are", self.color.count('red'), "gumballs of type red in the machine")
        elif type_ == 'green':
            print("There are", self.color.count('green'), "gumballs of type green in the machine")
        elif type_ == 'blue':
            print("There are", self.color.count('blue'), "gumballs of type blue in the machine")
        print()

# TESTER CODE

machine = Gumball_Machine(5)
machine.report()

machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")

machine.dispense(0.10)
machine.dispense(0.50)
machine.dispense(0.01)

machine.report()

machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")

machine.dispense(0.25)
machine.dispense(0.25)
machine.dispense(0.25)

machine.report()

machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")

machine.dispense(0.25)
machine.dispense(0.25)
machine.dispense(0.25)

machine.report()

machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")
