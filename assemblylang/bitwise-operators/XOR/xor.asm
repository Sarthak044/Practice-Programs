section .data

section .text
    global _start

_start:
      
    mov eax, 0x10
    xor eax, 0x11

    ; Exit program 
    mov eax, 1
    mov ebx, 0
    int 0x80