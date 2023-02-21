section .data
    num1 dq 20          ; First operand
    num2 dq 10          ; Second operand
    result dq 0         ; Initialize result to 0
    
section .text
    global _start

_start:
    mov ebx, [num1]     
    mov eax, [num2]
    mul ebx

   
    ; Exit program 
    mov eax, 1
    mov ebx, 0
    int 0x80