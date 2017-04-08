import sys
import threading
import time

# This is a simple implementanio of the PIA 6821 chip which provided
# parallel IO to the 6502 chip and of the two peripherals attached 
# to it on the original Apple 1 -- the display and the keyboard.
# I have not studied the schematics to see how closely this implements
# the actual hardware behaviour, but it is adequate to bring up Integer
# Basic and all the Apple 1 software I have tried so far.

# I based it largely on reverse engineering the Wozmon.

class PIA6821(threading.Thread):
    def __init__(self, decoder, terminal):

        # register the display register and its control register
        decoder.registerReader(0xd012, self.dsp_read)
        decoder.registerWriter(0xd012, self.dsp_write)
        
        decoder.registerReader(0xd013, self.dspcr_read)
        decoder.registerWriter(0xd013, self.dspcr_write)

        # and the same for the keyboard register
        decoder.registerReader(0xd010, self.kbd_read)
        decoder.registerWriter(0xd010, self.kbd_write)

        decoder.registerReader(0xd011, self.kbdcr_read)
        decoder.registerWriter(0xd011, self.kbdcr_write)
        self.terminal = terminal

    # The display address when read 
    def dsp_read(self, addr):
        if self.terminal.dspready == True:
            return 0x80
        else:
            return 0x00
    
    # unlike the real display, we simply print characters as fast as
    # they come -- this should probably be configurable, in reality
    # writing to the register while the display hardware was running
    # would probably have scrambled the value stored 
    def dsp_write(self, addr, val):
        self.terminal.terminalprint(val)
        return
    
    # there is IO space for a DSP CR but it's not mapped to anything
    def dspcr_read(self, addr):
        return 0x00

    def dspcr_write(self, addr, val):
        return 0x00
    
    def kbd_read(self, addr):
        if self.terminal.charQueue.empty():
            return 0x80
        else:
            c = self.terminal.charQueue.get()
            if (self.terminal.charQueue.empty()):
                self.terminal.kbdready = False
            return c

    def kbd_write(self, addr, val):
        return

    def kbdcr_read(self, addr):
        if self.terminal.kbdready == True:
                return 0x80
        else:
                return 0x00

    def kbdcr_write(self, addr, val):
        return
