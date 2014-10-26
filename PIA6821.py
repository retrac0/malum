import sys
import threading
import time

class PIA6821(threading.Thread):
    def __init__(self, decoder, terminal):
        decoder.registerReader(0xd012, self.dsp_read)
        decoder.registerWriter(0xd012, self.dsp_write)
        
        decoder.registerReader(0xd013, self.dspcr_read)
        decoder.registerWriter(0xd013, self.dspcr_write)

        decoder.registerReader(0xd010, self.kbd_read)
        decoder.registerWriter(0xd010, self.kbd_write)

        decoder.registerReader(0xd011, self.kbdcr_read)
        decoder.registerWriter(0xd011, self.kbdcr_write)
        self.terminal = terminal

    def dsp_read(self, addr):
        if self.terminal.dspready == True:
            return 0x80
        else:
            return 0x00

    def dsp_write(self, addr, val):
#        print("dsp write :", hex(val & 0x7f))
        self.terminal.terminalprint(val)
        return

    def dspcr_read(self, addr):
        return 0x00

    def dspcr_write(self, addr, val):
        return 0x00
    
    def kbd_read(self, addr):
        if self.terminal.char == None:
            return 0x80
        else:
            self.terminal.kbdready = False
            return self.terminal.char

    def kbd_write(self, addr, val):
        return

    def kbdcr_read(self, addr):
        if self.terminal.kbdready == True:
                return 0x80
        else:
                return 0x00

    def kbdcr_write(self, addr, val):
        return
