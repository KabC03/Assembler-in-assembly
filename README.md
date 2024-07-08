# Assembler-in-assembly



An EXTREMELY basic x86 assembler written in assembly language (x86).

A hashmap is used to convert pneumonics -> machine code output

### ISA:

#### Registers
    EAX, EBX, ECX, EDX - All 32 bit registers

#### Immediates

    - Immediates take the form of (+-)DIGIT. 
    - It MUST be signed irreguardless of if the immediate is positive or negativea
    - The Immediate itself must be a single digit 0-9


#### [R]
    ADD Rx Ry          - Add the contents of Ry and Rz, placing the result into Rx


#### [I]
    LIR Rx Imm          - Load an immediate 'Imm' into the register Rx
    PSH Rx              - Push Rx onto the stack
    POP Rx              - Pop from the stack into Rx


#### [J]
    JEQ Rx Ry Imm       - Jump 'Imm' number of instructions if Rx == Ry









