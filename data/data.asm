; Defines section

%define LINE_BUFFER_SIZE 1000



; .data section
section .data



; .bss section
section .bss
    valueBuffer: db 10
; .text section
section .text

initialise_hashmap:
    push eax
    lea edi, [valueBuffer]
    mov dword [edi], 65686876
    mov dword [edi], 73828083
    mov word [edi], 7280
