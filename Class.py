class Computer:

    def __init__(self, CPU, RAM):
        self.CPU = CPU
        self.RAM = RAM

    def config(self):
        print('Configuration: ', self.CPU, self.RAM)

    def update(self, CPU):
        self.CPU = CPU

comp1 = Computer('i5', '16 GB')
#print(type(comp1))

Computer.config(comp1);
comp1.update('i3')
Computer.config(comp1);
# Alternative to call class method
#comp1.config()
