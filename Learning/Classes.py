class computer:
    def __init__(self, cpu, ram, mbd, gpu):
        self.cpu = cpu
        self.ram = ram
        self.mbd = mbd
        self.gpu = gpu

    def print2(self, value):
        print(str(value))