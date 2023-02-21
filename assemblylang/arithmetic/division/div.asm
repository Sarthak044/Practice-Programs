section .data
    num1 dq 20         ; First operand
    num2 dq 5          ; Second operand
    result dq 0         ; Initialize result to 0
    
section .text
    global _start

_start:
    mov edx, 0     
    mov eax, [num1]
    mov ecx, [num2]
    div ecx

   
    ; Exit program 
    mov eax, 1
    mov ebx, 0
    int 0x80