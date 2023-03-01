section .data
 
section .text
    global _start
    
_start:
    mov eax, 10
    cmp eax, 0
    jnz else_if
    mov eax, 5
    jmp short end
    else_if:
    cmp eax, 1
    jnz else
    mov eax, 6
    jmp short end
    else:
    mov eax , 7
    
    end:
        ; Exit program 
        mov eax, 1
        mov ebx, 0
        int 0x80