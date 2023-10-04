# Generated from TerceraParte.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TerceraParteParser import TerceraParteParser
else:
    from TerceraParteParser import TerceraParteParser

# This class defines a complete generic visitor for a parse tree produced by TerceraParteParser.

class TerceraParteVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TerceraParteParser#prog.
    def visitProg(self, ctx:TerceraParteParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TerceraParteParser#Mod.
    def visitMod(self, ctx:TerceraParteParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TerceraParteParser#Mov.
    def visitMov(self, ctx:TerceraParteParser.MovContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TerceraParteParser#Rot.
    def visitRot(self, ctx:TerceraParteParser.RotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TerceraParteParser#blank.
    def visitBlank(self, ctx:TerceraParteParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TerceraParteParser#AsignMod.
    def visitAsignMod(self, ctx:TerceraParteParser.AsignModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TerceraParteParser#SntxMov.
    def visitSntxMov(self, ctx:TerceraParteParser.SntxMovContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TerceraParteParser#INT.
    def visitINT(self, ctx:TerceraParteParser.INTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TerceraParteParser#SntxRot.
    def visitSntxRot(self, ctx:TerceraParteParser.SntxRotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TerceraParteParser#SntxRotOp.
    def visitSntxRotOp(self, ctx:TerceraParteParser.SntxRotOpContext):
        return self.visitChildren(ctx)



del TerceraParteParser