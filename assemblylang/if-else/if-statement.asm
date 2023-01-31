section .data
    ;x db 10  

section .text
    global _start

_start:
    cmp dword [x], 0
    jne else
    mov dword [x], 5
    jmp end
    else:
        mov dword [x], 1
    end:
    