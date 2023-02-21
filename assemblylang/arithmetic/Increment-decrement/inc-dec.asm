section .data
    num1 dq 20          
    num2 dq 5
section .text
    global _start

_start:
      
    ; INCREMENT
    mov eax, [num1]
    inc eax

    ;DECREMENT
    mov ebx, [num2]
    dec ebx

    ; Exit program 
    mov eax, 1
    mov ebx, 0
    int 0x80