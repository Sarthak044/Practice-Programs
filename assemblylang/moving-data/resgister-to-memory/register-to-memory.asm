global _start

section .data
sample: db 0xaa, 0xbb, 0xbb, 0xcc, 0xdd, 0xee, 0xff, 0x11, 0x22

section .text
_start:

    mov eax, 0x33445566
    mov byte [sample], al
    mov word [sample], ax
    mov dword [sample], eax
    
    ; Exit program 
    mov eax, 1
    mov ebx, 0
    int 0x80