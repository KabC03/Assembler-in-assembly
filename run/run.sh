#!/bin/bash

# This is a template file for assembling and running .asm files with nasm (x86 - 32 bit architecture)

programName="program.asm"


nasm -f elf32 -o program.o $programName

ld -m elf_i386 -o program program.o

./program


echo "Program returned: $?"

 
