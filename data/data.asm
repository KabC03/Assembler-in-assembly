; This file contains various buffers and definitions used by the assembler

; File processing
%define LINE_BUFFER_SIZE 1000

; Hashmap
%define HASH_TABLE_SIZE 100
%define KEY_LENGTH 3
%define DJB2_HASH_SEED 5381


section .data

	; Keys
	; Instructions
	key_add: db "add" ; Add instruction
	key_lir: db "lir" ; Load immediate instruction
	key_psh: db "psh" ; Push instruction	
	key_pop: db "pop" ; Pop instruction
	key_jeq: db "jeq" ; Jump if equal instruction
	key_blk: db "blk" ; Blank marker -> value = 0

	; Registers
	key_eax: db "eax" ; eax register
	key_ebx: db "ebx" ; ebx register	
	key_ecx: db "ecx" ; ecx register
	key_edx: db "edx" ; edx register
	


	; Values - Machine code
	; Instrurctions


	; Registers


section .bss
	
	line_buffer: resb LINE_BUFFER_SIZE
	




