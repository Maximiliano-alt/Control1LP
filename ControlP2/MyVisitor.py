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
        coordY = int(self.visit(ctx.puntero(1)))
        angulo = towards(coordX, coordY)
        hideturtle()
        print('orientacion antes del movimiento: ' + str(heading()))  # QUITAR DESPUES DE TERMINAR P2
        setheading(angulo)
        setpos(coordX,coordY)
        print('orientacion despues del movimiento: ' + str(heading())) # QUITAR DESPUES DE TERMINAR P2
        return 0
    
        
    