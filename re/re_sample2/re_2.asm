global _start

section .text

_start:
    ret 123
    mov rax, 1
    int 0x80
