from SegundaParteVisitor import SegundaParteVisitor
from SegundaParteParser import SegundaParteParser
from turtle import *

class MyVisitor(SegundaParteVisitor):
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
    
    def visitINT(self, ctx):
        return ctx.INT().getText()
    
    def visitAsignMod(self, ctx):
        if ctx.op.type == SegundaParteParser.ENC:
            pendown()
            return 0
        else:
            penup()
            return 0
    
    def visitPos(self, ctx):
        coordX = int(self.visit(ctx.puntero(0)))
        if ctx.puntero(1) != None:
            coordY = int(self.visit(ctx.puntero(1)))
        else:
            coordY = None

        #hideturtle()
        if ctx.op.type == SegundaParteParser.MOV:
            if coordY != None:
                angulo = towards(coordX, coordY)
                setheading(angulo)
                setpos(coordX,coordY)
                return 0
            else:
                forward(coordX)
        elif ctx.op.type == SegundaParteParser.ROT:
            if coordY != None:
                angulo = towards(coordX, coordY)
                setheading(angulo)
                return 0
            else:
                orientacion = heading()
                setheading(coordX + orientacion)
        return 0
    
        
    