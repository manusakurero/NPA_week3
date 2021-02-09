class Router:
    def __init__(self, brand, model, hostname):
        self.brand = brand
        self.model = model
        self.hostname = hostname
        self.interfaces = []
    def add_inf(self,interface):
        self.interfaces.append(interface)
    def show_infs(self):
        for i in self.interfaces:
            #show_inf = 'Show interfaces of ' + self.hostname + '\n' + self.interfaces.count
            print(i)

r1 = Router('Cisco', 'IOSv', 'R1')
r2 = Router('Cisco', '3745', 'R2')
r3 = Router('Juniper', 'MX5', 'R3')

r1.add_inf('Gigabit 0/1')
r1.add_inf('Gigabit 0/2')
r2.add_inf('Gigabit 0/1')
r2.add_inf('Gigabit 0/2')
r2.add_inf('Gigabit 0/3')
r3.add_inf('Gigabit 0/1')

print(r1.show_infs())
print(r2.show_infs())
print(r3.show_infs())

