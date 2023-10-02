# Generated from PrimeraParte.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PrimeraParteParser import PrimeraParteParser
else:
    from PrimeraParteParser import PrimeraParteParser

# This class defines a complete generic visitor for a parse tree produced by PrimeraParteParser.

class PrimeraParteVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PrimeraParteParser#prog.
    def visitProg(self, ctx:PrimeraParteParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrimeraParteParser#Mod.
    def visitMod(self, ctx:PrimeraParteParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrimeraParteParser#Dib.
    def visitDib(self, ctx:PrimeraParteParser.DibContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrimeraParteParser#blank.
    def visitBlank(self, ctx:PrimeraParteParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrimeraParteParser#AsignMod.
    def visitAsignMod(self, ctx:PrimeraParteParser.AsignModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrimeraParteParser#Pos.
    def visitPos(self, ctx:PrimeraParteParser.PosContext):
        return self.visitChildren(ctx)



del PrimeraParteParser