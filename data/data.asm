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
    mov ebp, esp
    push edi
    lea edi, [valueBuffer]
    mov dword [edi], 65686876
    add edi, 4
    mov dword [edi], 73828083
    add edi, 4
    mov word [edi], 7280
    add edi, 2
    mov esp, ebp
    ret



