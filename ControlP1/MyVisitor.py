from PrimeraParteVisitor import PrimeraParteVisitor
from PrimeraParteParser import PrimeraParteParser
from turtle import *

class MyVisitor(PrimeraParteVisitor):
    def __init__(self):
        self.memory = {}

    # Realizacion del comando para determinar el modo del puntero (encendido/apagado)
    def visitMod(self, ctx):
        value = self.visit(ctx.modo())
        print(value)
        return 0
    
    # Realización del comando para el trazado en el plano
    def visitDib(self, ctx):
        value = self.visit(ctx.puntero())
        print(value)
        return 0

    # Determinación del Modo del puntero
    def visitAsignMod(self, ctx):
        # Modo encendido
        if ctx.op.type == PrimeraParteParser.ENC:
            pendown()
            return 0
        # Modo apagado
        else:
            penup()
            return 0
    
    # Movimiento del puntero hacia la coordenada especificada
    def visitPos(self, ctx):
        # Determinación de coordenadas
        coordX = int(ctx.INT(0).getText())
        coordY = int(ctx.INT(1).getText())
        hideturtle()
        setpos(coordX,coordY)
        return 0
    
        
    
