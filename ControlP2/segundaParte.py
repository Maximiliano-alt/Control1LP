import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from SegundaParteLexer import SegundaParteLexer
from SegundaParteParser import SegundaParteParser
from MyVisitor import MyVisitor
from turtle import *

if __name__ == '__main__':
    while (True):
        if len(sys.argv) > 1:
            input_stream = FileStream(sys.argv[1])
        else:
            print("Ingresar comandos:")
            input_stream = InputStream(sys.stdin.readline())
        lexer = SegundaParteLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = SegundaParteParser(token_stream)
        tree = parser.prog()
        visitor = MyVisitor()
        visitor.visit(tree)