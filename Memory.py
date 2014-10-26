class Decoder:
    def __init__(self):
        self.readerDict = {}
        self.writerDict = {}
        for i in range (0, 0x10000):
            self.readerDict[i] = self.notDecodedRead
            self.writerDict[i] = self.notDecodedWrite
        return

    def __getitem__(self, address):
        return self.readerDict[address](address)

    def __setitem__(self, address, value):
        self.writerDict[address](address, value)
        return

    def registerReader(self, address, func):
        self.readerDict[address] = func
        return

    def registerWriter(self, address, func):
        self.writerDict[address] = func
        return

    def notDecodedRead(self, address):
        return 0xff

    def notDecodedWrite(self, address, func):
        return

class Memory:
    def __init__(self, decoder, offset, size):
        self.size = size
        self.mem = [0] * size
        self.offset = offset
        for i in range(0, size):
            decoder.registerReader(i + offset, self.__getitem__)
            decoder.registerWriter(i + offset, self.__setitem__)
        return
    
    def __getitem__(self, address):
        return self.mem[address - self.offset]

    def load(self, f):
        for i in range(0, self.size):
            t = f.read(1)
            if t == b'':
                t = 0
            else:
                t = ord(t)
            self.mem[i] = t

class RAM(Memory):
    def __setitem__(self, address, value):
        self.mem[address - self.offset] = value
        return

class ROM(Memory):
    def __setitem__(self, address, value):
        return
