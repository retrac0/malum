import py65.devices.mpu6502

import threading
import time

# this is just a simple wrapper for the py65 library

class Processor:
    def __init__(self, d):
        self.decoder = d
        self.mpu = py65.devices.mpu6502.MPU(self.decoder, 0xff00)
        self.running = True
        self.reset = False
    
    def stoprunning(self):
        print("processor stopped")
        self.running = False

    def run(self):
        while (self.running):
            if self.reset == True:
                self.reset = False
                self.mpu.reset()
            time.sleep(0.000005)
            self.mpu.step()
