from TerceraParteVisitor import TerceraParteVisitor
from TerceraParteParser import TerceraParteParser
from turtle import *

class MyVisitor(TerceraParteVisitor):
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
        if ctx.op.type == TerceraParteParser.ENC:
            pendown()
            return 0
        else:
            penup()
            return 0
    
    def visitPos(self, ctx):
        coordX = int(ctx.INT(0).getText())
        coordY = int(ctx.INT(1).getText())
        angulo2 = int(ctx.INT(2).getText())
        #hideturtle()
        angulo = towards(coordX, coordY)
        setheading(angulo)
        setpos(coordX,coordY)
        setheading(angulo)
        left(angulo2)
        return 0
    
        
    
