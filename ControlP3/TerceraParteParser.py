# Generated from TerceraParte.g4 by ANTLR 4.13.1
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
        4,1,12,58,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,26,8,1,
        1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,35,8,3,1,3,1,3,3,3,39,8,3,1,4,1,
        4,1,4,1,4,1,4,3,4,46,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,56,
        8,4,1,4,0,0,5,0,2,4,6,8,0,2,1,0,6,7,1,0,4,5,60,0,11,1,0,0,0,2,25,
        1,0,0,0,4,27,1,0,0,0,6,38,1,0,0,0,8,55,1,0,0,0,10,12,3,2,1,0,11,
        10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,1,1,0,0,
        0,15,16,3,4,2,0,16,17,5,11,0,0,17,26,1,0,0,0,18,19,3,6,3,0,19,20,
        5,11,0,0,20,26,1,0,0,0,21,22,3,8,4,0,22,23,5,11,0,0,23,26,1,0,0,
        0,24,26,5,11,0,0,25,15,1,0,0,0,25,18,1,0,0,0,25,21,1,0,0,0,25,24,
        1,0,0,0,26,3,1,0,0,0,27,28,7,0,0,0,28,5,1,0,0,0,29,30,5,8,0,0,30,
        31,5,1,0,0,31,34,5,10,0,0,32,33,5,2,0,0,33,35,5,10,0,0,34,32,1,0,
        0,0,34,35,1,0,0,0,35,36,1,0,0,0,36,39,5,3,0,0,37,39,5,10,0,0,38,
        29,1,0,0,0,38,37,1,0,0,0,39,7,1,0,0,0,40,41,5,9,0,0,41,42,5,1,0,
        0,42,45,5,10,0,0,43,44,5,2,0,0,44,46,5,10,0,0,45,43,1,0,0,0,45,46,
        1,0,0,0,46,47,1,0,0,0,47,56,5,3,0,0,48,49,5,9,0,0,49,50,5,1,0,0,
        50,51,3,6,3,0,51,52,7,1,0,0,52,53,3,6,3,0,53,54,5,3,0,0,54,56,1,
        0,0,0,55,40,1,0,0,0,55,48,1,0,0,0,56,9,1,0,0,0,6,13,25,34,38,45,
        55
    ]

class TerceraParteParser ( Parser ):

    grammarFileName = "TerceraParte.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'+'", "'-'", "'encendido'", 
                     "'apagado'", "'mover'", "'rotar'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SUM", "REST", "ENC", "APAG", "MOV", "ROT", "INT", 
                      "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_dibujo = 1
    RULE_modo = 2
    RULE_movimiento = 3
    RULE_rotacion = 4

    ruleNames =  [ "prog", "dibujo", "modo", "movimiento", "rotacion" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    SUM=4
    REST=5
    ENC=6
    APAG=7
    MOV=8
    ROT=9
    INT=10
    NEWLINE=11
    WS=12

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
                return self.getTypedRuleContexts(TerceraParteParser.DibujoContext)
            else:
                return self.getTypedRuleContext(TerceraParteParser.DibujoContext,i)


        def getRuleIndex(self):
            return TerceraParteParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = TerceraParteParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.dibujo()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4032) != 0)):
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
            return TerceraParteParser.RULE_dibujo

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ModContext(DibujoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TerceraParteParser.DibujoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def modo(self):
            return self.getTypedRuleContext(TerceraParteParser.ModoContext,0)

        def NEWLINE(self):
            return self.getToken(TerceraParteParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMod" ):
                return visitor.visitMod(self)
            else:
                return visitor.visitChildren(self)


    class BlankContext(DibujoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TerceraParteParser.DibujoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(TerceraParteParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class MovContext(DibujoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TerceraParteParser.DibujoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def movimiento(self):
            return self.getTypedRuleContext(TerceraParteParser.MovimientoContext,0)

        def NEWLINE(self):
            return self.getToken(TerceraParteParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMov" ):
                return visitor.visitMov(self)
            else:
                return visitor.visitChildren(self)


    class RotContext(DibujoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TerceraParteParser.DibujoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def rotacion(self):
            return self.getTypedRuleContext(TerceraParteParser.RotacionContext,0)

        def NEWLINE(self):
            return self.getToken(TerceraParteParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRot" ):
                return visitor.visitRot(self)
            else:
                return visitor.visitChildren(self)



    def dibujo(self):

        localctx = TerceraParteParser.DibujoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_dibujo)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7]:
                localctx = TerceraParteParser.ModContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.modo()
                self.state = 16
                self.match(TerceraParteParser.NEWLINE)
                pass
            elif token in [8, 10]:
                localctx = TerceraParteParser.MovContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.movimiento()
                self.state = 19
                self.match(TerceraParteParser.NEWLINE)
                pass
            elif token in [9]:
                localctx = TerceraParteParser.RotContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.rotacion()
                self.state = 22
                self.match(TerceraParteParser.NEWLINE)
                pass
            elif token in [11]:
                localctx = TerceraParteParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 24
                self.match(TerceraParteParser.NEWLINE)
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
            return TerceraParteParser.RULE_modo

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AsignModContext(ModoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TerceraParteParser.ModoContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def ENC(self):
            return self.getToken(TerceraParteParser.ENC, 0)
        def APAG(self):
            return self.getToken(TerceraParteParser.APAG, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignMod" ):
                return visitor.visitAsignMod(self)
            else:
                return visitor.visitChildren(self)



    def modo(self):

        localctx = TerceraParteParser.ModoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_modo)
        self._la = 0 # Token type
        try:
            localctx = TerceraParteParser.AsignModContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==6 or _la==7):
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
            return TerceraParteParser.RULE_movimiento

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SntxMovContext(MovimientoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TerceraParteParser.MovimientoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MOV(self):
            return self.getToken(TerceraParteParser.MOV, 0)
        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(TerceraParteParser.INT)
            else:
                return self.getToken(TerceraParteParser.INT, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSntxMov" ):
                return visitor.visitSntxMov(self)
            else:
                return visitor.visitChildren(self)


    class INTContext(MovimientoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TerceraParteParser.MovimientoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(TerceraParteParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitINT" ):
                return visitor.visitINT(self)
            else:
                return visitor.visitChildren(self)



    def movimiento(self):

        localctx = TerceraParteParser.MovimientoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_movimiento)
        self._la = 0 # Token type
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                localctx = TerceraParteParser.SntxMovContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.match(TerceraParteParser.MOV)
                self.state = 30
                self.match(TerceraParteParser.T__0)
                self.state = 31
                self.match(TerceraParteParser.INT)
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 32
                    self.match(TerceraParteParser.T__1)
                    self.state = 33
                    self.match(TerceraParteParser.INT)


                self.state = 36
                self.match(TerceraParteParser.T__2)
                pass
            elif token in [10]:
                localctx = TerceraParteParser.INTContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.match(TerceraParteParser.INT)
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
            return TerceraParteParser.RULE_rotacion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SntxRotOpContext(RotacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TerceraParteParser.RotacionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def ROT(self):
            return self.getToken(TerceraParteParser.ROT, 0)
        def movimiento(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TerceraParteParser.MovimientoContext)
            else:
                return self.getTypedRuleContext(TerceraParteParser.MovimientoContext,i)

        def REST(self):
            return self.getToken(TerceraParteParser.REST, 0)
        def SUM(self):
            return self.getToken(TerceraParteParser.SUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSntxRotOp" ):
                return visitor.visitSntxRotOp(self)
            else:
                return visitor.visitChildren(self)


    class SntxRotContext(RotacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TerceraParteParser.RotacionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ROT(self):
            return self.getToken(TerceraParteParser.ROT, 0)
        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(TerceraParteParser.INT)
            else:
                return self.getToken(TerceraParteParser.INT, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSntxRot" ):
                return visitor.visitSntxRot(self)
            else:
                return visitor.visitChildren(self)



    def rotacion(self):

        localctx = TerceraParteParser.RotacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_rotacion)
        self._la = 0 # Token type
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = TerceraParteParser.SntxRotContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(TerceraParteParser.ROT)
                self.state = 41
                self.match(TerceraParteParser.T__0)
                self.state = 42
                self.match(TerceraParteParser.INT)
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 43
                    self.match(TerceraParteParser.T__1)
                    self.state = 44
                    self.match(TerceraParteParser.INT)


                self.state = 47
                self.match(TerceraParteParser.T__2)
                pass

            elif la_ == 2:
                localctx = TerceraParteParser.SntxRotOpContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.match(TerceraParteParser.ROT)
                self.state = 49
                self.match(TerceraParteParser.T__0)
                self.state = 50
                self.movimiento()
                self.state = 51
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==4 or _la==5):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 52
                self.movimiento()
                self.state = 53
                self.match(TerceraParteParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





