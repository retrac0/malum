Malum - Apple 1 Emulator
------------------------

Malum is a simple Apple 1 emulator in Python.

It requires the py65.  It can either be on the system path or in the current directory.  It can be installed with the Python package manager pip or can be found at https://github.com/mnaberez/py65 and cloned with git.  For example: 

    % git clone https://github.com/mnaberez/py65.git py65.git
    % cp -a py65.git/py65 . 

At present, it emulates an Apple 1 with 4 KB of RAM at 0 and the Woz monitor at 0xFF00, or a Replica 1 with 32 KB of RAM, 8 KB of ROM including Integer BASIC at E000, Krusader assembler at F000 and the Woz monitor at FF00

To run:

    python Malum.py -m replica1

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

Todo:

* Load and save RAM (binary and ASCII wozmon format)
* non-hardcoded paths
* verify accuracy
* multiple models (4k Apple 1, 8K Apple 1, Replica-1, etc.)
