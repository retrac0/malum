import Memory
import PIA6821
import Terminal
import Processor

import time
import threading

decoder = Memory.Decoder()

processor = Processor.Processor(decoder)

ram = Memory.RAM(decoder, 0, 0x1000)
basicrom = Memory.ROM(decoder, 0xe000, 0x1000)
rom = Memory.ROM(decoder, 0xff00, 0x100)
rom.load(open("roms/wozmon.bin", "rb"))
basicrom.load(open("roms/basic.bin", "rb"))

terminal = Terminal.Terminal(processor)

pia = PIA6821.PIA6821(decoder, terminal)

termthread = threading.Thread(target=terminal.run)
procthread = threading.Thread(target=processor.run)

termthread.start()
procthread.start()
