
.intel_syntax noprefix
.comm	tape,4000,32
.global main
main:
    mov rax, 0
    lea rax, tape
    
    mov rbx,1
    add [rax],rbx
            

    mov rbx,1
    add [rax],rbx
            

    mov rbx,1
    add [rax],rbx
            

    mov rbx,1
    add [rax],rbx
            

    mov rbx,1
    add [rax],rbx
            

    mov rbx,1
    add [rax],rbx
            

    mov rbx,1
    add [rax],rbx
            

    mov rbx,1
    add [rax],rbx
            

    mov rbx,1
    add [rax],rbx
            

.Lbegin1:
    mov rbx, 0
    cmp [rax], rbx
    je .Lend1
    
    mov rbx,1
    sub [rax],rbx
            

    add  rax,8
            

    mov rbx,1
    add [rax],rbx
            

    sub  rax,8
            
    jmp .Lbegin1
.Lend1:
        

    add  rax,8
            
    mov rax, [rax]
    ret
    