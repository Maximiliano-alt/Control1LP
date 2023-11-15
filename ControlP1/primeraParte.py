import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from PrimeraParteLexer import PrimeraParteLexer
from PrimeraParteParser import PrimeraParteParser
from MyVisitor import MyVisitor
from turtle import *

if __name__ == '__main__':
    while (True):
        if len(sys.argv) > 1:
            input_stream = FileStream(sys.argv[1])
        else:
            print("Ingresar comandos:")
            input_stream = InputStream(sys.stdin.readline())
        lexer = PrimeraParteLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = PrimeraParteParser(token_stream)
        tree = parser.prog()
        visitor = MyVisitor()
        visitor.visit(tree)