import threading
import Getch

import sys
import time

# courtesy https://stackoverflow.com/questions/510357/python-read-a-single-character-from-the-user

class Terminal(threading.Thread):
    def __init__(self, p):
        self.processor = p
        self.char = None
        self.kbdready = False
        self.dspready = True

    # take an integer value as written to memory, 
    # passed on by the PIA6821 chip and clear its high bit,
    def fromApple1(self, val):
        # strip high bit
        val = val & 0x7f
        val = chr(val)
        return val

    def toApple1(self, val):
        val = val.upper()
        val = ord(val)
        val = val | 0x80
        return val

    def terminalprint(self, val):
        self.dspready = False
        val = self.fromApple1(val)
        sys.stdout.write(val)
        if val == '\r':
            sys.stdout.write('\n')
        sys.stdout.flush()
        time.sleep(0.0166)


    def run (self):
        while (1):
            c = Getch.getch()
#           print("getch: ", hex(self.char))
            self.kbdready = True
            if c == chr(0x05):      # ^E
                self.processor.reset = True
            if c == chr(0x03):      # ^C
                print("Exiting")
                sys.exit()
            self.char = self.toApple1(c)
