import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from TerceraParteLexer import TerceraParteLexer
from TerceraParteParser import TerceraParteParser
from MyVisitor import MyVisitor
from turtle import *

if __name__ == '__main__':
    while (True):
        if len(sys.argv) > 1:
            input_stream = FileStream(sys.argv[1])
        else:
            print("Ingrese coordenadas => rotar(mover(x,y)+angulo) :")
            input_stream = InputStream(sys.stdin.readline())
        lexer = TerceraParteLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = TerceraParteParser(token_stream)
        tree = parser.prog()
        visitor = MyVisitor()
        visitor.visit(tree)