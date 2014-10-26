#!/usr/bin/python3

import Memory
import PIA6821
import Terminal
import Processor

import argparse
import threading

parser = argparse.ArgumentParser(description="Apple 1 Emulator")
parser.add_argument("-m", "--model",
        help="set model to apple1 (default) or replica1",
        default="apple1")
parser.add_argument("-w", "--writerom",
        help="allow writes to ROM (default: false)", 
        type=bool, default=False)
parser.add_argument("-r", "--ramsize",
        help="set ram size in KB (default: 4 KB for apple1, 32 KB for replica1)",
        type=int, default=0)

args = parser.parse_args()

decoder = Memory.Decoder()

processor = Processor.Processor(decoder)

# default options for an apple 1
ramsize = 4 * 1024
rompath = "roms/wozmon.bin"
rombase = 0xff00
romsize = 0x100

if args.model == "apple1":
    ramsize = 4 * 1024
    rompath = "roms/wozmon.bin"
    rombase = 0xff00
    romsize = 0x100

if args.model == "replica1":
    ramsize = 32 * 1024
    rompath = "roms/replica1.bin"
    rombase = 0xe000
    romsize = 0x2000

if args.ramsize != 0:
    ramsize = args.ramsize * 1024

print ("Ramsize: ", ramsize)

ram = Memory.RAM(decoder, 0, ramsize) 
rom = Memory.ROM(decoder, rombase, romsize)
rom.load(open(rompath, "rb"))

terminal = Terminal.Terminal(processor)

pia = PIA6821.PIA6821(decoder, terminal)

termthread = threading.Thread(target=terminal.run)
procthread = threading.Thread(target=processor.run)

termthread.start()
procthread.start()
