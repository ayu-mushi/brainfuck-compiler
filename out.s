
.intel_syntax noprefix
.comm	tape,4000,32
.comm	input1,4000,32
.global main
main:
    mov r8, 0
    lea r8, tape

    mov r10, 0
    lea r10, input1

    mov rax, 0              # specify read system call
    mov edx, 2000            # 3nd argument (count)
    mov rsi, r10              # 2nd argument (string pointer)
    mov edi, 0x0            # 1st argument (stdout)
    syscall


    mov rbx, [r10]
    mov [r8], rbx
    add r10, 1
            

    add  r8,8
            

    mov rbx, [r10]
    mov [r8], rbx
    add r10, 1
            

    sub  r8,8
            

.Lbegin1:
    mov rbx, 0
    cmp [r8], rbx
    je .Lend1

    mov rbx,1
    sub [r8],rbx
            

    add  r8,8
            

    mov rbx,1
    add [r8],rbx
            

    sub  r8,8
            
    jmp .Lbegin1
.Lend1:
        

    add  r8,8
            

    mov rax, 1
    mov edx, 0x1
    mov rsi,r8
    mov edi,0x1
    syscall
            

    mov rax, [r8]
    ret
    