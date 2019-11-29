#!/usr/bin/python3
# coding: utf-8
# Brainfuckインタプリタを作成した。
# gccがsubprocessから実行できることが必要(Linux推奨)

from lark import Tree, Transformer, Visitor, exceptions
from lark import Lark
# pip install lark-parser

class State():
    def __init__(self, n, input_code):
        self.pointer = 0
        self.ram = list(map(lambda x: 0, range(0, n)))
        self.output = []
        self.input_code = input_code
    @property
    def present_value(self):
        return self.ram[self.pointer]
    @present_value.setter
    def present_value(self, value):
        self.ram[self.pointer] = value
    def show_result(self):
        return "".join(list(map(chr, self.output)))
    def show_state(self):
        return "input: "+ str(self.input_code) + "\noutput: "+ str(self.output) + "\nram: " + str(self.ram) + "\npointer: " + str(self.pointer)

def createState(n):
    yn = input("インプットを数字で入力したい場合はy, 文字列で入力したい場合はnを押してね: ")
    if(yn=="y"):
        return State(n, list(map(int, input("数字で入力 (434,123,434,233): ").split(","))))
    elif(yn=="n"):
        return State(n, list(map(ord, input("文字列を入力してみてね: "))))
    else:
        print("yかnで入力してください")

def inc(state):
    state.ram[state.pointer] += 1
def dec(state):
    state.ram[state.pointer] -= 1
def left(state):
    state.pointer -= 1
def right(state):
    state.pointer += 1
def output_process(state):
    state.output.append(state.present_value)
def input_process(state):
    state.present_value = state.input_code.pop()

inst_dict = {"+": inc,
             "-": dec,
             "<": left,
             ">": right,
             ".": output_process,
             ",": input_process}

def composition(f, g):
    def h(state):
        f(state)
        g(state)
        return state
    return h

def loop_process(program):
    def l(state):
        while(state.present_value != 0):
            program(state)
    return l


class Interpret(Transformer):
    """aaa"""
    def atomic_inst(self, args):
        #print("inst: ", args)
        instruct = args[0]
        #print(instruct)
        return inst_dict[instruct]
    def inst(self, args):
        return args[0]
    def loop(self, args):
        return (loop_process(args[0]))
    def program(self, args):
        #print("program: ", args)
        #assert tree.data == "+"
        #print(tree.children[0].children[0])
        if(len(args) == 1):
            return args[0]
        elif(len(args) == 2):
            return composition(args[0], args[1])

label_number = 0
def get_label_number():
    global label_number
    label_number += 1
    return label_number

class Compile(Transformer):
    """aaa"""
    def atomic_inst(self, args):
        instruct = args[0]
        if(args[0] == "+"):
            s="""
    mov rbx,1
    add [r8],rbx
            """
        elif (args[0] == "-"):
            s="""
    mov rbx,1
    sub [r8],rbx
            """
        elif (args[0] == "<"):
            s="""
    sub  r8,8
            """
        elif (args[0] == ">"):
            s="""
    add  r8,8
            """
        elif (args[0] == "."):
            s="""
    mov rax, 1
    mov edx, 0x1
    mov rsi,r8
    mov edi,0x1
    syscall
            """

        elif (args[0] == ","):
            s="""
    #mov rbx, [r10]
    #mov [r8], rbx
    #add r10, 8
            """
        return s
    def inst(self, args):
        return args[0]

    def loop(self, args):
        s = """
.Lbegin{0}:
    mov rbx, 0
    cmp [r8], rbx
    je .Lend{0}
    {1}
    jmp .Lbegin{0}
.Lend{0}:
        """
        return s.format(get_label_number(), args[0])
    def program(self, args):
        #print("program: ", args)
        #assert tree.data == "+"
        #print(tree.children[0].children[0])
        if(len(args) == 1):
            return args[0]
        elif(len(args) == 2):
            return args[0] + "\n" + args[1]

def bf_parser():
    try:
        #program = open("program2.bf").read()
        try:
            program = open(input("ファイル名を入力(デフォルトはprogram.bf): ")).read()
        except FileNotFoundError:
            print("program.bf")
            program = open("program.bf").read()
        rule = open("grammer.txt").read()

        parser = Lark(rule, start="program", parser="lalr")


        tree = parser.parse(program)

        return tree

    except exceptions.UnexpectedCharacters as e:
        print("予期しない文字が含まれています:")
        print(e)
        raise exceptions.UnexpectedCharacters


def bf_intepreter(tree):
    state = createState(100)
    executable = Interpret().transform(tree)
    executable(state)

    print("", state.show_state())
    print("output:", state.show_result())

def bf_compiler(tree):
    s = """
.intel_syntax noprefix
.comm	tape,4000,32
.comm	input1,40,8
.global main
main:
    mov r8, 0
    lea r8, tape

    # input
    mov r10, 0
    lea r10, input1
    mov rax, 0              # specify read system call
    mov edx, 1            # 3nd argument (count)
    mov rsi, input1              # 2nd argument (string pointer)
    mov edi, 0x0            # 1st argument (stdout)
    syscall

    {0}
    mov rax, [r10]
    ret
    """
    main_code = Compile().transform(tree)
    with open("out.s", mode="w") as f:
        f.write(s.format(main_code, input("入力")))
    import subprocess
    # gcc が必要
    subprocess.run("gcc -static -o out out.s".split(" "))

#bf_intepreter(bf_parser())
bf_compiler(bf_parser())
