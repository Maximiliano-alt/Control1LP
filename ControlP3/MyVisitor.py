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
        if ctx.op.type == TerceraParteParser.ENC:
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
            return angulo
        else:
            forward(coordX)
        return heading()
    
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
        forward(200)
        #setheading(izq)
        print('orientacion despues de izq:', heading())
        der = float(self.visit(ctx.movimiento(1)))
        print('orientacion despues de der:', heading())
        print('esperado: 90 -> resultado: ', izq)
        print('esperado: 135 -> resultado: ', der)
        if ctx.op.type == TerceraParteParser.SUM:
            orientacion = heading()
            setheading(izq+der)
            return 0
        else:
            orientacion = heading()
            setheading(izq-der)
        return 0
    
        
    