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
    
    def visitAsignMod(self, ctx):
        if ctx.op.type == SegundaParteParser.ENC:
            pendown()
            return 0
        else:
            penup()
            return 0
    
    def visitMov(self, ctx):
        coordX = int(ctx.INT(0).getText())
        if ctx.INT(1) != None:
            coordY = int(ctx.INT(1).getText())
        else:
            coordY = None

        #hideturtle()
        if coordY != None:
            angulo = towards(coordX, coordY)
            setheading(angulo)
            setpos(coordX,coordY)
            return 0
        else:
            forward(coordX)
        return 0
    
    def visitRot(self, ctx):
        coordX = int(ctx.INT(0).getText())
        if ctx.INT(1) != None:
            coordY = int(ctx.INT(1).getText())
        else:
            coordY = None
            
        #hideturtle()
        if coordY != None:
            angulo = towards(coordX, coordY)
            setheading(angulo)
            return 0
        else:
            orientacion = heading()
            setheading(coordX + orientacion)
        return 0
    
        
    