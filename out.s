
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


    mov rbx,1
    add [r8],rbx
            

    mov rbx,1
    add [r8],rbx
            

    mov rbx,1
    add [r8],rbx
            

    mov rbx,1
    add [r8],rbx
            

    add  r8,8
            

    mov rbx,1
    add [r8],rbx
            

    mov rbx,1
    add [r8],rbx
            

    mov rbx,1
    add [r8],rbx
            

    mov rbx,1
    add [r8],rbx
            

    sub  r8,8
            

.Lbegin2:
    mov rbx, 0
    cmp [r8], rbx
    je .Lend2

    mov rbx,1
    sub [r8],rbx
            

    add  r8,8
            

    mov rbx,1
    add [r8],rbx
            

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
        

    sub  r8,8
            
    jmp .Lbegin2
.Lend2:
        

    add  r8,8
            

    add  r8,8
            

    mov rax, [r8]
    ret
    