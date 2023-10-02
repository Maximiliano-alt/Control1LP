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


    # Visit a parse tree produced by TerceraParteParser#Dib.
    def visitDib(self, ctx:TerceraParteParser.DibContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TerceraParteParser#blank.
    def visitBlank(self, ctx:TerceraParteParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TerceraParteParser#AsignMod.
    def visitAsignMod(self, ctx:TerceraParteParser.AsignModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TerceraParteParser#Pos.
    def visitPos(self, ctx:TerceraParteParser.PosContext):
        return self.visitChildren(ctx)



del TerceraParteParser