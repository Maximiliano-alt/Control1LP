from PrimeraParteVisitor import PrimeraParteVisitor
from PrimeraParteParser import PrimeraParteParser
from turtle import *

class MyVisitor(PrimeraParteVisitor):
    def __init__(self):
        self.memory = {}

    def visitMod(self, ctx):
        value = self.visit(ctx.modo())
        print(value)
        return 0
    
    def visitDib(self, ctx):
        value = self.visit(ctx.puntero())
        print(value)
        return 0

    def visitAsignMod(self, ctx):
        if ctx.op.type == PrimeraParteParser.ENC:
            pendown()
            return 0
        else:
            penup()
            return 0
    
    def visitPos(self, ctx):
        coordX = int(ctx.INT(0).getText())
        coordY = int(ctx.INT(1).getText())
        hideturtle()
        setpos(coordX,coordY)
        return 0
    
        
    
