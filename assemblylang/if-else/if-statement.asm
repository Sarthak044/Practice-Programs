section .data
    x dq 10  

section .text
    global _start

_start:
    cmp dword [x], 0
    jne end_if
    mov dword [x], 5
    end_if:
        mov dword [x], 2

    ; Exit program 
    mov eax, 1
    mov ebx, 0
    int 0x80
    