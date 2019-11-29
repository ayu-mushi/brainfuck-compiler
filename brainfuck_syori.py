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


def bf_intepreter():
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

        state = createState(100)
        executable = Interpret().transform(tree)
        executable(state)

        print("", state.show_state())
        print("output:", state.show_result())

    except exceptions.UnexpectedCharacters:
        print("予期しない文字が含まれています")


def bf_compiler():
    s = """
.intel_syntax noprefix
.global main
main:
    mov rax, {0}
    ret
    """.format("2434")
    with open("out.s", mode="w") as f:
        f.write(s)
    import subprocess
    # gcc が必要
    subprocess.run("gcc -o out out.s".split(" "))

bf_compiler()
#print(tree)
