section .data
 

section .text
    global _start

_start:
    mov eax, 10
    cmp eax, 0
    jne end_if
    mov eax, 5
    end_if:
        mov eax, 2

    ; Exit program 
    mov eax, 1
    mov ebx, 0
    int 0x80
    