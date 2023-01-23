section .data
    x db 10  

section .text
    global _start

_start:
    mov eax, [x]    
    cmp eax, 0     
    je else         
    mov byte [x], 5 
    jmp end         

else:
    mov byte [x], 1 

end:
    