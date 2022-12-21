section .data
    ;db stands for define bytes, it means that we are going to define some raw bytes of data into our code
    ; each character in the string is single byte. The 10 is a newline character
    text db "Hello World!",10
section .text
    global _start

_start:
    mov rax ,1
    mov rdi ,1
    mov rsi ,text
    mov rdx ,14
    syscall

    mov rax, 60
    mov rdi, 0
    syscall