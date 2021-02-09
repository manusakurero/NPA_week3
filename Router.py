class Router:
    def __init__(self, brand, model, hostname):
        self.brand = brand
        self.model = model
        self.hostname = hostname
        self.interfaces = []
        self.connection = []
    def add_inf(self, interface):
        self.interfaces.append(interface)
    def show_infs(self):
        total_interfaces = ''
        for i in self.interfaces:
            total_interfaces += i+'\n'
        show_infsv = 'Show interfaces of ' + self.hostname + '\nR3 has ' + str(len(self.interfaces)) +' Interfaces\n'+ total_interfaces
        return show_infsv
    def connect(self, interface1, router, interface2):
        self.connection.append([interface1, router.hostname, interface2])
        router.connection.append([interface2, self.hostname, interface1])
    def show_cdp(self):
        show_cdpv = ''
        for i in self.connection:
           show_cdpv += self.hostname + ' interface '+i[0]+' connect to '+i[1]+' on interface '+i[2]+'\n'
        return show_cdpv

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

r1.connect('Gigabit 0/1', r2, 'Gigabit 0/2')
r1.connect('Gigabit 0/2', r3, 'Gigabit 0/1')
print(r1.show_cdp())
print(r2.show_cdp())
print(r3.show_cdp())

