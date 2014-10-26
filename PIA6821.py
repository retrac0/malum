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
#        print("dsp read")
        return 0x0

    def dsp_write(self, addr, val):
#        print("dsp write :", hex(val & 0x7f))
        self.terminal.dspready = False
        self.terminal.terminalprint(val)
        time.sleep(0.0166)
        return

    def dspcr_read(self, addr):
        return

    def dspcr_write(self, addr, val):
        return
    
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
