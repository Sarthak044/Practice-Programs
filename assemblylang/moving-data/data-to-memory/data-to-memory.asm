global _start

section .data
sample: db 0xaa, 0xbb, 0xbb, 0xcc, 0xdd, 0xee, 0xff, 0x11, 0x22


section .text
_start:

    mov dword [sample], 0x33445566
    
    ; Exit program 
    mov eax, 1
    mov ebx, 0
    int 0x80

