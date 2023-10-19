import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from CuartaParteLexer import CuartaParteLexer
from CuartaParteParser import CuartaParteParser
from MyVisitor import MyVisitor
from turtle import *

if __name__ == '__main__':
    while (True):
        if len(sys.argv) > 1:
            input_stream = FileStream(sys.argv[1])
        else:
            print("Ingrese coordenadas (x,y,encendido|apagado):")
            input_stream = InputStream(sys.stdin.readline())
        lexer = CuartaParteLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = CuartaParteParser(token_stream)
        tree = parser.prog()
        visitor = MyVisitor()
        visitor.visit(tree)