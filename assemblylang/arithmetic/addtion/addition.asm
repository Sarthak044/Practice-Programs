section .data
    num1 dq 10          ; First operand
    num2 dq 20          ; Second operand
    result dq 0         ; Initialize result to 0
    
section .text
    global _start

_start:
    mov rax, [num1]     ; Move the first operand to the RAX register
    add rax, [num2]     ; Add the second operand to the RAX register
    mov [result], rax   ; Move the result from the RAX register to the result variable

   
    ; Exit program 
    mov eax, 1
    mov ebx, 0
    int 0x80