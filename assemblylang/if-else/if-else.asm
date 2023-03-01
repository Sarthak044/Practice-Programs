section .data
 
section .text
    global _start

_start:
    mov eax, 2
    cmp eax, 0
    je else
    mov eax, 5
    else:
        mov eax, 1
    
    end:
        ; Exit program 
        mov eax, 1
        mov ebx, 0
        int 0x80