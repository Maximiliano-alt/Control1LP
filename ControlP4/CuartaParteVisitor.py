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


    # Visit a parse tree produced by CuartaParteParser#Mov.
    def visitMov(self, ctx:CuartaParteParser.MovContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CuartaParteParser#Rot.
    def visitRot(self, ctx:CuartaParteParser.RotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CuartaParteParser#Rep.
    def visitRep(self, ctx:CuartaParteParser.RepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CuartaParteParser#blank.
    def visitBlank(self, ctx:CuartaParteParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CuartaParteParser#AsignMod.
    def visitAsignMod(self, ctx:CuartaParteParser.AsignModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CuartaParteParser#SntxMov.
    def visitSntxMov(self, ctx:CuartaParteParser.SntxMovContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CuartaParteParser#INT.
    def visitINT(self, ctx:CuartaParteParser.INTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CuartaParteParser#SntxRot.
    def visitSntxRot(self, ctx:CuartaParteParser.SntxRotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CuartaParteParser#SntxRotOp.
    def visitSntxRotOp(self, ctx:CuartaParteParser.SntxRotOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CuartaParteParser#SntxRepMov.
    def visitSntxRepMov(self, ctx:CuartaParteParser.SntxRepMovContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CuartaParteParser#SntxRepRot.
    def visitSntxRepRot(self, ctx:CuartaParteParser.SntxRepRotContext):
        return self.visitChildren(ctx)



del CuartaParteParser