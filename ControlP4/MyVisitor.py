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
    
    def visitMov(self, ctx):
        value = self.visit(ctx.movimiento())
        print(value)
        return 0
    
    def visitRot(self, ctx):
        value = self.visit(ctx.rotacion())
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
    
    def visitSntxMov(self, ctx):
        coordX = int(ctx.INT(0).getText())      #int(self.visit(ctx.puntero(0)))
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
    
    def visitSntxRot(self, ctx):
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
    
    def visitSntxRotOp(self, ctx):
        izq = float(self.visit(ctx.movimiento(0)))
        der = float(self.visit(ctx.movimiento(1)))
        orientacion = heading()
        if ctx.op.type == CuartaParteParser.SUM:
            print(izq + der)
            setheading(orientacion + izq + der)
            heading()
            return 0
        elif ctx.op.type == CuartaParteParser.REST:
            print(izq - der)
            setheading(orientacion + (izq - der))
            heading()
            return 0
        return 0
    
    def visitSntxRepMov(self, ctx):
        rep = int(ctx.INT().getText())
        x = 0
        while x < rep:
            self.visit(ctx.movimiento())
            x += 1
        return 0
    
    def visitSntxRepRot(self, ctx):
        rep = int(ctx.INT().getText())
        x = 0
        while x < rep:
            self.visit(ctx.rotacion())
            x += 1
        return 0
    
        
    