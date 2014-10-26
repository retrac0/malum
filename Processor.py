import MPU6502

import threading
import time

class Processor:
    def __init__(self, d):
        self.decoder = d
        self.mpu = MPU6502.MPU(self.decoder, 0xff00)
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
