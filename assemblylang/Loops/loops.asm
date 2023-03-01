section .data

section .text
    global _start
    
_start:
    mov ebx,0
    while_start:
        cmp ebx,5
    jge end
    mov eax, ebx
    add eax, 1
    mov ebx, eax
    jmp while_start
    
    end:
         ;Exit program 
            mov eax, 1
            mov ebx, 0
            int 0x80