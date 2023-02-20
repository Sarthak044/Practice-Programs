section .data
    num1 dq 10          ; First operand
    num2 dq 20          ; Second operand
    result dq 0         ; Initialize result to 0
    outmsg db "The result is: %d", 10, 0  ; Output message format

section .text
    global _start

_start:
    mov rax, [num1]     ; Move the first operand to the RAX register
    add rax, [num2]     ; Add the second operand to the RAX register
    mov [result], rax   ; Move the result from the RAX register to the result variable

    ; Output the result
    mov rdi, outmsg     ; Move the output message format to the RDI register
    mov rsi, [result]   ; Move the result to the RSI register
    xor eax, eax        ; Clear RAX register
    call printf         ; Call the C standard library printf function
    
    ; Exit program
    mov eax, 60         ; Exit syscall number
    xor edi, edi        ; Exit status code 0
    syscall             ; Perform system call
