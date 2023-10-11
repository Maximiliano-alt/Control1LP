from CuartaParteVisitor import CuartaParteVisitor
from CuartaParteParser import CuartaParteParser
from turtle import *

class MyVisitor(CuartaParteVisitor):
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
        if ctx.op.type == CuartaParteParser.ENC:
            pendown()
            return 0
        else:
            penup()
            return 0
    
    def visitPos(self, ctx):
        a=0
        while a != MyVisitor.visitRep():
            coordX = int(self.visit(ctx.puntero(0)))
            if ctx.puntero(1) != None:
                coordY = int(self.visit(ctx.puntero(1)))
            else:
                coordY = None

            #hideturtle()
            if ctx.op.type == CuartaParteParser.MOV:
                if coordY != None:
                    angulo = towards(coordX, coordY)
                    setheading(angulo)
                    setpos(coordX,coordY)
                    return 0
                else:
                    forward(coordX)
            elif ctx.op.type == CuartaParteParser.ROT:
                if coordY != None:
                    angulo = towards(coordX, coordY)
                    setheading(angulo)
                    return 0
                else:
                    orientacion = heading()
                    setheading(coordX + orientacion)
            a=a+1
        return 0
    
    def visitAng(self, ctx):
        coordX = int(self.visit(ctx.puntero(0)))
        coordY = int(self.visit(ctx.puntero(1)))
        if ctx.op.type == CuartaParteParser.SUM:
            ang = int(self.visit(ctx.puntero(2)))
            angulo = towards(coordX, coordY)
            setheading(angulo)
            setpos(coordX,coordY)
            left(ang)
        elif ctx.op.type == CuartaParteParser.RES:
            ang = int(self.visit(ctx.puntero(2)))
            angulo = towards(coordX, coordY)
            setheading(angulo)
            setpos(coordX,coordY)
            right(ang)
        return 0
    
        
    