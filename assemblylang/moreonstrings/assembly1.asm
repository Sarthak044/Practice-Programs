section .data
    ; count the length of the string till 0 [dynamic]
    text db "Hello World!",10,0

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

;input : rax
; output: print string at rax

_print:
    push rax
    mov rbx, 0

_printLoop:
    inc rax
    inc rbx
    mov cl, [rax]
    cmp cl,0
    jne _printLoop
    mov rax, 1
    mov rdi, 1
    pop rsi
    mov rdx, rbx
    syscall
    ret