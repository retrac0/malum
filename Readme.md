Malum - An Apple 1 Emulator
---------------------------

Malum is a simple Apple 1 emulator in Python, using the py65 CPU core
written by Mike Naberezny.

To run:

    python Malum.py

Control-E is reset, control-C exits.  \ is the Woz monitor reset prompt.  You can read more about the Woz monitor at http://sbprojects.com/projects/apple1/wozmon.php

Example where the first 32 bytes of Integer Basic are first dumped, Integer BASIC is then run, a small BASIC program is entered and then executed.

    \
    E000.E01F
    
    E000: 4C B0 E2 AD 11 D0 10 FB
    E008: AD 10 D0 60 8A 29 20 F0
    E010: 23 A9 A0 85 E4 4C C9 E3
    E018: A9 20 C5 24 B0 0C A9 8D
    E000R
    
    E000: 4C
    >10 PRINT "HELLO"
    >20 END
    >LIST
       10 PRINT "HELLO"
       20 END 

    >RUN
    HELLO

