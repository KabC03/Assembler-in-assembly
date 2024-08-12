; 12 Aug, 2024
section .text




; edx polymap_get_value(eax key)
polymap_get_value:

    mov ebp, esp

; Setup
    push ebp
    push eax
    push ebx
    push ecx




; Evaluate polynomial at eax

    mov edx, eax
    sub edx, 76

    mov ebx, eax
    sub ebx, 74
    mul edx, ebx
    mov ebx, eax
    sub ebx, 88
    mul edx, ebx
    mov ebx, eax
    sub ebx, 89
    mul edx, ebx
    mul edx, 48
    div edx, 54648

    mov ecx, eax
    sub ecx, 65

    mov ebx, eax
    sub ebx, 74
    mul ecx, ebx
    mov ebx, eax
    sub ebx, 88
    mul ecx, ebx
    mov ebx, eax
    sub ebx, 89
    mul ecx, ebx
    mul ecx, 49
    div ecx, 3432
    add edx, ecx

    mov ecx, eax
    sub ecx, 65

    mov ebx, eax
    sub ebx, 76
    mul ecx, ebx
    mov ebx, eax
    sub ebx, 88
    mul ecx, ebx
    mov ebx, eax
    sub ebx, 89
    mul ecx, ebx
    mul ecx, 50
    div ecx, -3780
    add edx, ecx

    mov ecx, eax
    sub ecx, 65

    mov ebx, eax
    sub ebx, 76
    mul ecx, ebx
    mov ebx, eax
    sub ebx, 74
    mul ecx, ebx
    mov ebx, eax
    sub ebx, 89
    mul ecx, ebx
    mul ecx, 48
    div ecx, -3864
    add edx, ecx

    mov ecx, eax
    sub ecx, 65

    mov ebx, eax
    sub ebx, 76
    mul ecx, ebx
    mov ebx, eax
    sub ebx, 74
    mul ecx, ebx
    mov ebx, eax
    sub ebx, 88
    mul ecx, ebx
    mul ecx, 49
    div ecx, 4680
    add edx, ecx






; Cleanup
    mov esp, ebp
    pop ecx
    pop ebx
    pop eax
    pop ebp
    ret
