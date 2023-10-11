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
        4,1,13,54,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,23,8,1,1,2,1,2,1,3,
        1,3,1,3,1,4,1,4,1,4,1,4,1,4,3,4,35,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,52,8,4,1,4,0,0,5,0,2,4,6,8,
        0,3,1,0,4,5,1,0,6,7,1,0,8,9,54,0,11,1,0,0,0,2,22,1,0,0,0,4,24,1,
        0,0,0,6,26,1,0,0,0,8,51,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,13,
        1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,1,1,0,0,0,15,16,3,4,2,0,16,
        17,5,12,0,0,17,23,1,0,0,0,18,19,3,8,4,0,19,20,5,12,0,0,20,23,1,0,
        0,0,21,23,5,12,0,0,22,15,1,0,0,0,22,18,1,0,0,0,22,21,1,0,0,0,23,
        3,1,0,0,0,24,25,7,0,0,0,25,5,1,0,0,0,26,27,5,10,0,0,27,28,5,11,0,
        0,28,7,1,0,0,0,29,30,7,1,0,0,30,31,5,1,0,0,31,34,3,8,4,0,32,33,5,
        2,0,0,33,35,3,8,4,0,34,32,1,0,0,0,34,35,1,0,0,0,35,36,1,0,0,0,36,
        37,5,3,0,0,37,52,1,0,0,0,38,39,5,7,0,0,39,40,5,1,0,0,40,41,5,6,0,
        0,41,42,5,1,0,0,42,43,3,8,4,0,43,44,5,2,0,0,44,45,3,8,4,0,45,46,
        5,3,0,0,46,47,7,2,0,0,47,48,3,8,4,0,48,49,5,3,0,0,49,52,1,0,0,0,
        50,52,5,11,0,0,51,29,1,0,0,0,51,38,1,0,0,0,51,50,1,0,0,0,52,9,1,
        0,0,0,4,13,22,34,51
    ]

class CuartaParteParser ( Parser ):

    grammarFileName = "CuartaParte.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'encendido'", "'apagado'", 
                     "'mover'", "'rotar'", "'+'", "'-'", "'Repetir'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ENC", "APAG", "MOV", "ROT", "SUM", "RES", "REP", 
                      "INT", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_dibujo = 1
    RULE_modo = 2
    RULE_repetir = 3
    RULE_puntero = 4

    ruleNames =  [ "prog", "dibujo", "modo", "repetir", "puntero" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    ENC=4
    APAG=5
    MOV=6
    ROT=7
    SUM=8
    RES=9
    REP=10
    INT=11
    NEWLINE=12
    WS=13

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
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.dibujo()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6384) != 0)):
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


    class DibContext(DibujoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CuartaParteParser.DibujoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def puntero(self):
            return self.getTypedRuleContext(CuartaParteParser.PunteroContext,0)

        def NEWLINE(self):
            return self.getToken(CuartaParteParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDib" ):
                return visitor.visitDib(self)
            else:
                return visitor.visitChildren(self)



    def dibujo(self):

        localctx = CuartaParteParser.DibujoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_dibujo)
        try:
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5]:
                localctx = CuartaParteParser.ModContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.modo()
                self.state = 16
                self.match(CuartaParteParser.NEWLINE)
                pass
            elif token in [6, 7, 11]:
                localctx = CuartaParteParser.DibContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.puntero()
                self.state = 19
                self.match(CuartaParteParser.NEWLINE)
                pass
            elif token in [12]:
                localctx = CuartaParteParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 21
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
            self.state = 24
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
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


    class RepetirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CuartaParteParser.RULE_repetir

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RepContext(RepetirContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CuartaParteParser.RepetirContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REP(self):
            return self.getToken(CuartaParteParser.REP, 0)
        def INT(self):
            return self.getToken(CuartaParteParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRep" ):
                return visitor.visitRep(self)
            else:
                return visitor.visitChildren(self)



    def repetir(self):

        localctx = CuartaParteParser.RepetirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_repetir)
        try:
            localctx = CuartaParteParser.RepContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(CuartaParteParser.REP)
            self.state = 27
            self.match(CuartaParteParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PunteroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CuartaParteParser.RULE_puntero

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PosContext(PunteroContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CuartaParteParser.PunteroContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def puntero(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CuartaParteParser.PunteroContext)
            else:
                return self.getTypedRuleContext(CuartaParteParser.PunteroContext,i)

        def MOV(self):
            return self.getToken(CuartaParteParser.MOV, 0)
        def ROT(self):
            return self.getToken(CuartaParteParser.ROT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPos" ):
                return visitor.visitPos(self)
            else:
                return visitor.visitChildren(self)


    class AngContext(PunteroContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CuartaParteParser.PunteroContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def ROT(self):
            return self.getToken(CuartaParteParser.ROT, 0)
        def MOV(self):
            return self.getToken(CuartaParteParser.MOV, 0)
        def puntero(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CuartaParteParser.PunteroContext)
            else:
                return self.getTypedRuleContext(CuartaParteParser.PunteroContext,i)

        def SUM(self):
            return self.getToken(CuartaParteParser.SUM, 0)
        def RES(self):
            return self.getToken(CuartaParteParser.RES, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAng" ):
                return visitor.visitAng(self)
            else:
                return visitor.visitChildren(self)


    class INTContext(PunteroContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CuartaParteParser.PunteroContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(CuartaParteParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitINT" ):
                return visitor.visitINT(self)
            else:
                return visitor.visitChildren(self)



    def puntero(self):

        localctx = CuartaParteParser.PunteroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_puntero)
        self._la = 0 # Token type
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = CuartaParteParser.PosContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 30
                self.match(CuartaParteParser.T__0)
                self.state = 31
                self.puntero()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 32
                    self.match(CuartaParteParser.T__1)
                    self.state = 33
                    self.puntero()


                self.state = 36
                self.match(CuartaParteParser.T__2)
                pass

            elif la_ == 2:
                localctx = CuartaParteParser.AngContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.match(CuartaParteParser.ROT)
                self.state = 39
                self.match(CuartaParteParser.T__0)
                self.state = 40
                self.match(CuartaParteParser.MOV)
                self.state = 41
                self.match(CuartaParteParser.T__0)
                self.state = 42
                self.puntero()
                self.state = 43
                self.match(CuartaParteParser.T__1)
                self.state = 44
                self.puntero()
                self.state = 45
                self.match(CuartaParteParser.T__2)
                self.state = 46
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==8 or _la==9):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 47
                self.puntero()
                self.state = 48
                self.match(CuartaParteParser.T__2)
                pass

            elif la_ == 3:
                localctx = CuartaParteParser.INTContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.match(CuartaParteParser.INT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





