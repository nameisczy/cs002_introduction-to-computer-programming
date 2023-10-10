class Smartphone:
    def __init__(self, capacity, name):
        self.capacity = capacity
        self.available = capacity
        self.name = name
        self.app = {}

    def add_app(self, appname, appsize):
        if appname in self.app:
            print("Cannot install app, duplicate app")
        elif self.available < appsize:
            print("Cannot install app, no available space")
        else:
            self.available = self.available - appsize
            self.app[appname] = appsize

    def remove_app(self, appname):
        if appname in self.app:
            self.available = self.available + appsize
            self.app.pop(appname)
        else:
            print("App doesn't exist")

    def has_app(self, appname):
        if appname in self.app:
            return True
        else:
            return False

    def get_available_space(self):
        return self.available

    def report(self):
        print("Name:", self.name)
        print("Capacity:",self.capacity - self.available, "out of", self.capacity, "GB")
        print("Available space:", self.available)
        print("Apps installed:", len(self.app))
        for i in sorted(self.app.keys()):
            print("*",i, "is using",self.app[i], "GB")

size = int(input("Size of your new smartphone (32, 64 or 128 GB): "))
name = input("Smartphone name: ")
print("Smartphone created!")
Smartphone = Smartphone(size, name)
Smartphone.report()
while True:
    print()
    choice = input("(r)eport, (a)dd app, r(e)move app or (q)uit: ")
    if choice == 'a':
        appname = input("App name to add: ")
        appsize = int(input("App size in GB: "))
        Smartphone.add_app(appname, appsize)
    elif choice == 'r':
        Smartphone.report()
    elif choice == 'e':
        app_name = input("App name to remove: ")
        print("App removed:", app_name)
        Smartphone.remove_app(app_name)
    elif choice == 'q':
        print("Goodbye!")
        break
    
