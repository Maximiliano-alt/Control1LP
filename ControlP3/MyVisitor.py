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
    
    def visitINT(self, ctx):
        return ctx.INT().getText()
    
    def visitAsignMod(self, ctx):
        if ctx.op.type == TerceraParteParser.ENC:
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
        if ctx.op.type == TerceraParteParser.MOV:
            if coordY != None:
                angulo = towards(coordX, coordY)
                setheading(angulo)
                setpos(coordX,coordY)
                return 0
            else:
                forward(coordX)
        elif ctx.op.type == TerceraParteParser.ROT:
            if coordY != None:
                angulo = towards(coordX, coordY)
                setheading(angulo)
                return 0
            else:
                orientacion = heading()
                setheading(coordX + orientacion)
        return 0
    
    def visitAng(self, ctx):
        coordX = int(self.visit(ctx.puntero(0)))
        coordY = int(self.visit(ctx.puntero(1)))
        if ctx.op.type == TerceraParteParser.SUM:
            ang = int(self.visit(ctx.puntero(2)))
            angulo = towards(coordX, coordY)
            setheading(angulo)
            setpos(coordX,coordY)
            left(ang)
        elif ctx.op.type == TerceraParteParser.RES:
            ang = int(self.visit(ctx.puntero(2)))
            angulo = towards(coordX, coordY)
            setheading(angulo)
            setpos(coordX,coordY)
            right(ang)
        return 0
    
        
    