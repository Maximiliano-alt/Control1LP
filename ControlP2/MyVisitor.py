from SegundaParteVisitor import SegundaParteVisitor
from SegundaParteParser import SegundaParteParser
from turtle import *

class MyVisitor(SegundaParteVisitor):
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
        if ctx.op.type == SegundaParteParser.ENC:
            pendown()
            return 0
        # Modo apagado
        else:
            penup()
            return 0
    
    # Logica del Movimiento del puntero
    def visitMov(self, ctx):
        # Determinación de la cantidad de coordenadas de movimiento ingresadas y sus valores
        coordX = int(ctx.INT(0).getText())
        if ctx.INT(1) != None:
            coordY = int(ctx.INT(1).getText())
        else:
            coordY = None

        # Movimiento del puntero a una posición (X,Y) en el plano
        if coordY != None:
            angulo = towards(coordX, coordY)
            setheading(angulo)
            setpos(coordX,coordY)
            return 0
        # Movimiento del puntero X puntos hacia su orientacion
        else:
            forward(coordX)
        return 0
    
    # Logica de la rotacion del puntero
    def visitRot(self, ctx):
        # Determinación de la cantidad de coordenadas de rotacion ingresadas y sus valores
        coordX = int(ctx.INT(0).getText())
        if ctx.INT(1) != None:
            coordY = int(ctx.INT(1).getText())
        else:
            coordY = None
            
        # Rotacion hacia un punto (X,Y) en el plano
        if coordY != None:
            angulo = towards(coordX, coordY)
            setheading(angulo)
            return 0
        # Rotacion en X grados desde su orientacion actual
        else:
            orientacion = heading()
            setheading(coordX + orientacion)
        return 0
    
        
    