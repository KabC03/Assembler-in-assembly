#!/bin/bash


programName="program.asm"


nasm -f elf32 -o program.o $programName

ld -m elf_i386 -o program program.o

./program


echo "Program returned: $?"

 
