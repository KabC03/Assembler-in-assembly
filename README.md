# Assembler-in-assembly



An EXTREMELY basic assembler in assembly language.

It uses a hashmap as well as some basic string handling to assemble the language.

__### ISA:__



#### [R]
    ADD Rx Ry Rz        - Add the contents of Ry and Rz, placing the result into Rx


#### [I]
    Li Rx Imm           - Load an immediate 'Imm' into Rx
    LOD Rx Ry           - Load 4 bytes from the address in Ry to Rx
    STR Rx Ry           - Store 4 bytes to the address in Ry from Rx


#### [J]
    JEQ Rx Ry Imm       - Jump to the address 'Imm' if the contents in Rx equals the contents of Ry









