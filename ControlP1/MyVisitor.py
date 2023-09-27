from PrimeraParteVisitor import PrimeraParteVisitor
from PrimeraParteParser import PrimeraParteParser
from turtle import *

class MyVisitor(PrimeraParteVisitor):
    def __init__(self):
        self.memory = {}
    
    def visitDib(self, ctx):
        value = self.visit(ctx.puntero())
        print(value)
        return 0
    
    def visitINT(self, ctx):
        return ctx.INT().getText()
    
    def visitPos(self, ctx):
        coordX = int(self.visit(ctx.puntero(0)))
        coordY = int(self.visit(ctx.puntero(1)))
        hideturtle()
        if ctx.op.type == PrimeraParteParser.ENC:
            pendown()
            setpos(coordX,coordY)
            return 0
        penup()
        setpos(coordX,coordY)
        return 0
    
        
    
