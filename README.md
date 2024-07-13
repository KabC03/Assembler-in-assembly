# Assembler-in-assembly



An EXTREMELY basic assembler written in assembly language (x86).


The goal of this project was more about learning how to write x86 rather than creating a proficient assembler.


It converts an x86-like ISA into machine code. Note the output file cannot be executed - since it is not in ELF format.


A hashmap is used to convert pneumonics -> machine code output.

### ISA:

#### Registers
    EAX, EBX, ECX, EDX - All 32 bit registers

#### Immediates

    - Immediates take the form of $(+-)DIGIT. 
    - It MUST be signed irreguardless of if the immediate is positive or negativea
    - The Immediate itself must be a single digit 0-9

    
    - E.g
    $+5 -> Immediate of +5
    $-2 -> Immediate of -2
    $+0 -> Immediate of 0
    $-0 -> Immediate of 0


#### BLK

    - BLK (blank) is padding to ensure all instructions are 4 * 3 = 12 bytes long

#### [R]egister
    ADD Rx Ry BLK       - Add the contents of Ry and Rz, placing the result into Rx


#### [I]mmediate
    LIR Rx Imm          - Load an immediate 'Imm' into the register Rx

#### [M]emory
    PSH Rx BLK          - Push Rx onto the stack
    POP Rx BLK          - Pop from the stack into Rx


#### [J]ump
    JEQ Rx Ry Imm       - Jump 'Imm' number of instructions if Rx == Ry







TODO:
- File handling in asm
- Read into a buffer of a fixed with and go line by line
- Hash the string
- Index into the hashmap array in data.asm
- Print that machine code to the output

