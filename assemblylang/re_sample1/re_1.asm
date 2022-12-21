global _start 

section .text

_start:
    ; this is a comment
    ; move data to rax register
    ; mov [detination], [source]
    mov rax, 10
    ;move data to rbx register
    mov rbx, 5
    add rax, rbx
    
    ; exit syscall
    mov rax, 1
    int 0x80

section .data
    ; used for declaring variables
