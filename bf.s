	.file	"bf.c"
	.intel_syntax noprefix
	.text
	.comm	tape,4000,32
	.comm	i,8,8
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp
	.cfi_def_cfa_register 6
	lea	rax, tape[rip]
	mov	QWORD PTR i[rip], rax
	mov	rax, QWORD PTR i[rip]
	movzx	edx, BYTE PTR [rax]
	add	edx, 1
	mov	BYTE PTR [rax], dl
	mov	rax, QWORD PTR i[rip]
	movzx	edx, BYTE PTR [rax]
	add	edx, 1
	mov	BYTE PTR [rax], dl
	mov	rax, QWORD PTR i[rip]
	movzx	edx, BYTE PTR [rax]
	add	edx, 1
	mov	BYTE PTR [rax], dl
	mov	rax, QWORD PTR i[rip]
	add	rax, 1
	mov	QWORD PTR i[rip], rax
	mov	eax, 0
	pop	rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 7.4.0-1ubuntu1~18.04.1) 7.4.0"
	.section	.note.GNU-stack,"",@progbits
