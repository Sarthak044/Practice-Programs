global _start

section .text
_start:

    mov eax, 10
    mov al, 0xbb
    mov ah, 0xcc
    mov ax, 0xdddd

    mov ebx, 0
    mov ecx, 0 

    ; Exit program 
    mov eax, 1
    mov ebx, 0
    int 0x80