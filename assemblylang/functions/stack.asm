section .data

section .text
    global _start

_start:
    push qword 3
    push qword 2
    call test
    add rsp, 16 ; after test is executed, the control is returned here
    xor eax, eax

test:
    push rbp
    mov rbp, rsp
    sub rsp, 16
    mov rax, qword [rbp+16]
    mov qword [rbp-8], rax
    mov rcx, qword [rbp+24]
    mov qword [rbp-16], rcx
    xor eax, eax
    mov rsp, rbp
    pop rbp
    ret

end:
    ; Exit program
    mov eax, 60
    xor edi, edi
    syscall
