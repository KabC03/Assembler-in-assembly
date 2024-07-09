; This file contains the code for the DJB2 hash function

section .data
	str: db "abc"
section .text
	global _start



_start:



	lea ebx, str
	call djb2_hash


	; Exit program
	mov eax, 1
	mov ebx, ecx
	int 0x80


; djb2_hash
; 
; Brief: Hashes a key of length KEY_LENGTH for a table of size HASH_TABLE_SIZE
;
; ebx -> Pointer to string to hash
; ecx -> Location of where the hash result is stored
djb2_hash:

	mov ebp, esp
	push eax	
	push ecx
	push edx
	
	mov ecx, DJB2_HASH_SEED
	
	mov eax, 0
FOR_START:	
	cmp eax, KEY_LENGTH
	je FOR_END

	imul ecx, 33

	; Add char byte
	movzx edx, byte [ebx + eax]	
	add ecx, edx


	inc eax
	jmp FOR_START
FOR_END:

	; Perform modulo
	mov eax, ecx
	xor edx, edx
	mov ebx, HASH_TABLE_SIZE
	div ebx 
	mov ecx, edx

	mov esp, ebp
	ret



