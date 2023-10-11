# Generated from CuartaParte.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CuartaParteParser import CuartaParteParser
else:
    from CuartaParteParser import CuartaParteParser

# This class defines a complete generic visitor for a parse tree produced by CuartaParteParser.

class CuartaParteVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CuartaParteParser#prog.
    def visitProg(self, ctx:CuartaParteParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CuartaParteParser#Mod.
    def visitMod(self, ctx:CuartaParteParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CuartaParteParser#Dib.
    def visitDib(self, ctx:CuartaParteParser.DibContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CuartaParteParser#blank.
    def visitBlank(self, ctx:CuartaParteParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CuartaParteParser#AsignMod.
    def visitAsignMod(self, ctx:CuartaParteParser.AsignModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CuartaParteParser#Rep.
    def visitRep(self, ctx:CuartaParteParser.RepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CuartaParteParser#Pos.
    def visitPos(self, ctx:CuartaParteParser.PosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CuartaParteParser#Ang.
    def visitAng(self, ctx:CuartaParteParser.AngContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CuartaParteParser#INT.
    def visitINT(self, ctx:CuartaParteParser.INTContext):
        return self.visitChildren(ctx)



del CuartaParteParser