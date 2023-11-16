from TerceraParteVisitor import TerceraParteVisitor
from TerceraParteParser import TerceraParteParser
from turtle import *

class MyVisitor(TerceraParteVisitor):
    def __init__(self):
        self.memory = {}
    
    # Realizacion del comando para determinar el modo del puntero (encendido/apagado)
    def visitMod(self, ctx):
        value = self.visit(ctx.modo())
        print(value)
        return 0
    
    # Realizacion del comando de movimiento en el plano
    def visitMov(self, ctx):
        value = self.visit(ctx.movimiento())
        print(value)
        return 0
    
    # Realizacion del comando de rotacion en el plano
    def visitRot(self, ctx):
        value = self.visit(ctx.rotacion())
        print(value)
        return 0
    
    # Identificacion por pantalla del valor entero ingresado 
    def visitINT(self, ctx):
        return ctx.INT().getText()
    
    # Determinación del Modo del puntero
    def visitAsignMod(self, ctx):
        if ctx.op.type == TerceraParteParser.ENC:
            pendown()
            return 0
        else:
            penup()
            return 0
    
    # Logica del Movimiento del puntero
    def visitSntxMov(self, ctx):
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
    def visitSntxRot(self, ctx):
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
    
    # Logica para la realizacion de la ejecucion de comandos como parametros de rotar()
    def visitSntxRotOp(self, ctx):
        # Realizacion de los comandos al interior de rotar() y almacenado de las salidas de estos
        izq = float(self.visit(ctx.movimiento(0)))
        der = float(self.visit(ctx.movimiento(1)))
        orientacion = heading()

        # Sumado de las salidas de izq y der para la rotacion
        if ctx.op.type == TerceraParteParser.SUM:
            print(izq + der)
            setheading(orientacion + izq + der)
            heading()
            return 0
        # Resta de las salidas de izq y der para la rotacion
        elif ctx.op.type == TerceraParteParser.REST:
            print(izq - der)
            setheading(orientacion + (izq - der))
            heading()
            return 0
        return 0
    
        
    