
.intel_syntax noprefix
.comm	tape,4000,32
.comm	input1,40,8
.global main
main:
    mov r8, 0
    lea r8, tape

    # input
    mov r10, input1
    mov rax, 0              # specify read system call
    mov edx, 1            # 3nd argument (count)
    mov rsi, input1              # 2nd argument (string pointer)
    mov edi, 0x0            # 1st argument (stdout)
    syscall

    
    #mov rbx, [r10]
    #mov [r8], rbx
    #add r10, 8
            

    mov rax, 1
    mov edx, 0x1
    mov rsi,r8
    mov edi,0x1
    syscall
            
    mov rax, [r10]
    ret
    