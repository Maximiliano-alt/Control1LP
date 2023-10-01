# Generated from SegundaParte.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SegundaParteParser import SegundaParteParser
else:
    from SegundaParteParser import SegundaParteParser

# This class defines a complete generic visitor for a parse tree produced by SegundaParteParser.

class SegundaParteVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SegundaParteParser#prog.
    def visitProg(self, ctx:SegundaParteParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SegundaParteParser#Mod.
    def visitMod(self, ctx:SegundaParteParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SegundaParteParser#Dib.
    def visitDib(self, ctx:SegundaParteParser.DibContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SegundaParteParser#blank.
    def visitBlank(self, ctx:SegundaParteParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SegundaParteParser#AsignMod.
    def visitAsignMod(self, ctx:SegundaParteParser.AsignModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SegundaParteParser#Mov.
    def visitMov(self, ctx:SegundaParteParser.MovContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SegundaParteParser#Rot.
    def visitRot(self, ctx:SegundaParteParser.RotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SegundaParteParser#INT.
    def visitINT(self, ctx:SegundaParteParser.INTContext):
        return self.visitChildren(ctx)



del SegundaParteParser