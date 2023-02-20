global _start

section .text
_start:

    mov ebx, eax
    mov cl, al 
    mov ch, ah
    mov cx, ax

    mov eax, 0 
    mov ebx, 0
    mov ecx, 0

    ; Exit program 
    mov eax, 1
    mov ebx, 0
    int 0x80
    