section .data
             
section .text
    global _start

_start:
      
    mov eax, 0xFFFFFFFF
    not eax
    not eax

    ; Exit program 
    mov eax, 1
    mov ebx, 0
    int 0x80