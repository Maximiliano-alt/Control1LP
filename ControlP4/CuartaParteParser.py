# Generated from CuartaParte.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,73,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,3,1,31,8,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,40,8,3,1,3,
        1,3,3,3,44,8,3,1,4,1,4,1,4,1,4,1,4,3,4,51,8,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,3,4,61,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,71,
        8,5,1,5,0,0,6,0,2,4,6,8,10,0,2,1,0,7,8,1,0,5,6,76,0,13,1,0,0,0,2,
        30,1,0,0,0,4,32,1,0,0,0,6,43,1,0,0,0,8,60,1,0,0,0,10,70,1,0,0,0,
        12,14,3,2,1,0,13,12,1,0,0,0,14,15,1,0,0,0,15,13,1,0,0,0,15,16,1,
        0,0,0,16,1,1,0,0,0,17,18,3,4,2,0,18,19,5,13,0,0,19,31,1,0,0,0,20,
        21,3,6,3,0,21,22,5,13,0,0,22,31,1,0,0,0,23,24,3,8,4,0,24,25,5,13,
        0,0,25,31,1,0,0,0,26,27,3,10,5,0,27,28,5,13,0,0,28,31,1,0,0,0,29,
        31,5,13,0,0,30,17,1,0,0,0,30,20,1,0,0,0,30,23,1,0,0,0,30,26,1,0,
        0,0,30,29,1,0,0,0,31,3,1,0,0,0,32,33,7,0,0,0,33,5,1,0,0,0,34,35,
        5,9,0,0,35,36,5,1,0,0,36,39,5,12,0,0,37,38,5,2,0,0,38,40,5,12,0,
        0,39,37,1,0,0,0,39,40,1,0,0,0,40,41,1,0,0,0,41,44,5,3,0,0,42,44,
        5,12,0,0,43,34,1,0,0,0,43,42,1,0,0,0,44,7,1,0,0,0,45,46,5,10,0,0,
        46,47,5,1,0,0,47,50,5,12,0,0,48,49,5,2,0,0,49,51,5,12,0,0,50,48,
        1,0,0,0,50,51,1,0,0,0,51,52,1,0,0,0,52,61,5,3,0,0,53,54,5,10,0,0,
        54,55,5,1,0,0,55,56,3,6,3,0,56,57,7,1,0,0,57,58,3,6,3,0,58,59,5,
        3,0,0,59,61,1,0,0,0,60,45,1,0,0,0,60,53,1,0,0,0,61,9,1,0,0,0,62,
        63,5,11,0,0,63,64,5,12,0,0,64,65,5,4,0,0,65,71,3,6,3,0,66,67,5,11,
        0,0,67,68,5,12,0,0,68,69,5,4,0,0,69,71,3,8,4,0,70,62,1,0,0,0,70,
        66,1,0,0,0,71,11,1,0,0,0,7,15,30,39,43,50,60,70
    ]

class CuartaParteParser ( Parser ):

    grammarFileName = "CuartaParte.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "':'", "'+'", "'-'", 
                     "'encendido'", "'apagado'", "'mover'", "'rotar'", "'repetir'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "SUM", "REST", "ENC", "APAG", "MOV", 
                      "ROT", "REP", "INT", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_dibujo = 1
    RULE_modo = 2
    RULE_movimiento = 3
    RULE_rotacion = 4
    RULE_repetir = 5

    ruleNames =  [ "prog", "dibujo", "modo", "movimiento", "rotacion", "repetir" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    SUM=5
    REST=6
    ENC=7
    APAG=8
    MOV=9
    ROT=10
    REP=11
    INT=12
    NEWLINE=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dibujo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CuartaParteParser.DibujoContext)
            else:
                return self.getTypedRuleContext(CuartaParteParser.DibujoContext,i)


        def getRuleIndex(self):
            return CuartaParteParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = CuartaParteParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.dibujo()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 16256) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DibujoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CuartaParteParser.RULE_dibujo

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ModContext(DibujoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CuartaParteParser.DibujoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def modo(self):
            return self.getTypedRuleContext(CuartaParteParser.ModoContext,0)

        def NEWLINE(self):
            return self.getToken(CuartaParteParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMod" ):
                return visitor.visitMod(self)
            else:
                return visitor.visitChildren(self)


    class BlankContext(DibujoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CuartaParteParser.DibujoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(CuartaParteParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class MovContext(DibujoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CuartaParteParser.DibujoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def movimiento(self):
            return self.getTypedRuleContext(CuartaParteParser.MovimientoContext,0)

        def NEWLINE(self):
            return self.getToken(CuartaParteParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMov" ):
                return visitor.visitMov(self)
            else:
                return visitor.visitChildren(self)


    class RotContext(DibujoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CuartaParteParser.DibujoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def rotacion(self):
            return self.getTypedRuleContext(CuartaParteParser.RotacionContext,0)

        def NEWLINE(self):
            return self.getToken(CuartaParteParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRot" ):
                return visitor.visitRot(self)
            else:
                return visitor.visitChildren(self)


    class RepContext(DibujoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CuartaParteParser.DibujoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def repetir(self):
            return self.getTypedRuleContext(CuartaParteParser.RepetirContext,0)

        def NEWLINE(self):
            return self.getToken(CuartaParteParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRep" ):
                return visitor.visitRep(self)
            else:
                return visitor.visitChildren(self)



    def dibujo(self):

        localctx = CuartaParteParser.DibujoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_dibujo)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8]:
                localctx = CuartaParteParser.ModContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.modo()
                self.state = 18
                self.match(CuartaParteParser.NEWLINE)
                pass
            elif token in [9, 12]:
                localctx = CuartaParteParser.MovContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.movimiento()
                self.state = 21
                self.match(CuartaParteParser.NEWLINE)
                pass
            elif token in [10]:
                localctx = CuartaParteParser.RotContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.rotacion()
                self.state = 24
                self.match(CuartaParteParser.NEWLINE)
                pass
            elif token in [11]:
                localctx = CuartaParteParser.RepContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.repetir()
                self.state = 27
                self.match(CuartaParteParser.NEWLINE)
                pass
            elif token in [13]:
                localctx = CuartaParteParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 29
                self.match(CuartaParteParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CuartaParteParser.RULE_modo

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AsignModContext(ModoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CuartaParteParser.ModoContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def ENC(self):
            return self.getToken(CuartaParteParser.ENC, 0)
        def APAG(self):
            return self.getToken(CuartaParteParser.APAG, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignMod" ):
                return visitor.visitAsignMod(self)
            else:
                return visitor.visitChildren(self)



    def modo(self):

        localctx = CuartaParteParser.ModoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_modo)
        self._la = 0 # Token type
        try:
            localctx = CuartaParteParser.AsignModContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MovimientoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CuartaParteParser.RULE_movimiento

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SntxMovContext(MovimientoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CuartaParteParser.MovimientoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MOV(self):
            return self.getToken(CuartaParteParser.MOV, 0)
        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(CuartaParteParser.INT)
            else:
                return self.getToken(CuartaParteParser.INT, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSntxMov" ):
                return visitor.visitSntxMov(self)
            else:
                return visitor.visitChildren(self)


    class INTContext(MovimientoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CuartaParteParser.MovimientoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(CuartaParteParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitINT" ):
                return visitor.visitINT(self)
            else:
                return visitor.visitChildren(self)



    def movimiento(self):

        localctx = CuartaParteParser.MovimientoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_movimiento)
        self._la = 0 # Token type
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                localctx = CuartaParteParser.SntxMovContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(CuartaParteParser.MOV)
                self.state = 35
                self.match(CuartaParteParser.T__0)
                self.state = 36
                self.match(CuartaParteParser.INT)
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 37
                    self.match(CuartaParteParser.T__1)
                    self.state = 38
                    self.match(CuartaParteParser.INT)


                self.state = 41
                self.match(CuartaParteParser.T__2)
                pass
            elif token in [12]:
                localctx = CuartaParteParser.INTContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(CuartaParteParser.INT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RotacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CuartaParteParser.RULE_rotacion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SntxRotOpContext(RotacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CuartaParteParser.RotacionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def ROT(self):
            return self.getToken(CuartaParteParser.ROT, 0)
        def movimiento(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CuartaParteParser.MovimientoContext)
            else:
                return self.getTypedRuleContext(CuartaParteParser.MovimientoContext,i)

        def REST(self):
            return self.getToken(CuartaParteParser.REST, 0)
        def SUM(self):
            return self.getToken(CuartaParteParser.SUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSntxRotOp" ):
                return visitor.visitSntxRotOp(self)
            else:
                return visitor.visitChildren(self)


    class SntxRotContext(RotacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CuartaParteParser.RotacionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ROT(self):
            return self.getToken(CuartaParteParser.ROT, 0)
        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(CuartaParteParser.INT)
            else:
                return self.getToken(CuartaParteParser.INT, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSntxRot" ):
                return visitor.visitSntxRot(self)
            else:
                return visitor.visitChildren(self)



    def rotacion(self):

        localctx = CuartaParteParser.RotacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_rotacion)
        self._la = 0 # Token type
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = CuartaParteParser.SntxRotContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.match(CuartaParteParser.ROT)
                self.state = 46
                self.match(CuartaParteParser.T__0)
                self.state = 47
                self.match(CuartaParteParser.INT)
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 48
                    self.match(CuartaParteParser.T__1)
                    self.state = 49
                    self.match(CuartaParteParser.INT)


                self.state = 52
                self.match(CuartaParteParser.T__2)
                pass

            elif la_ == 2:
                localctx = CuartaParteParser.SntxRotOpContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(CuartaParteParser.ROT)
                self.state = 54
                self.match(CuartaParteParser.T__0)
                self.state = 55
                self.movimiento()
                self.state = 56
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==5 or _la==6):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 57
                self.movimiento()
                self.state = 58
                self.match(CuartaParteParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepetirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CuartaParteParser.RULE_repetir

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SntxRepRotContext(RepetirContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CuartaParteParser.RepetirContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REP(self):
            return self.getToken(CuartaParteParser.REP, 0)
        def INT(self):
            return self.getToken(CuartaParteParser.INT, 0)
        def rotacion(self):
            return self.getTypedRuleContext(CuartaParteParser.RotacionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSntxRepRot" ):
                return visitor.visitSntxRepRot(self)
            else:
                return visitor.visitChildren(self)


    class SntxRepMovContext(RepetirContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CuartaParteParser.RepetirContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REP(self):
            return self.getToken(CuartaParteParser.REP, 0)
        def INT(self):
            return self.getToken(CuartaParteParser.INT, 0)
        def movimiento(self):
            return self.getTypedRuleContext(CuartaParteParser.MovimientoContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSntxRepMov" ):
                return visitor.visitSntxRepMov(self)
            else:
                return visitor.visitChildren(self)



    def repetir(self):

        localctx = CuartaParteParser.RepetirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_repetir)
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = CuartaParteParser.SntxRepMovContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.match(CuartaParteParser.REP)
                self.state = 63
                self.match(CuartaParteParser.INT)
                self.state = 64
                self.match(CuartaParteParser.T__3)
                self.state = 65
                self.movimiento()
                pass

            elif la_ == 2:
                localctx = CuartaParteParser.SntxRepRotContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.match(CuartaParteParser.REP)
                self.state = 67
                self.match(CuartaParteParser.INT)
                self.state = 68
                self.match(CuartaParteParser.T__3)
                self.state = 69
                self.rotacion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





