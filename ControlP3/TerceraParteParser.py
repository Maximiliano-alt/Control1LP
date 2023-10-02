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
        4,1,11,37,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,21,8,1,1,2,1,2,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,0,0,4,0,2,4,6,0,1,1,0,4,
        5,35,0,9,1,0,0,0,2,20,1,0,0,0,4,22,1,0,0,0,6,24,1,0,0,0,8,10,3,2,
        1,0,9,8,1,0,0,0,10,11,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,1,1,
        0,0,0,13,14,3,4,2,0,14,15,5,10,0,0,15,21,1,0,0,0,16,17,3,6,3,0,17,
        18,5,10,0,0,18,21,1,0,0,0,19,21,5,10,0,0,20,13,1,0,0,0,20,16,1,0,
        0,0,20,19,1,0,0,0,21,3,1,0,0,0,22,23,7,0,0,0,23,5,1,0,0,0,24,25,
        5,7,0,0,25,26,5,1,0,0,26,27,5,6,0,0,27,28,5,1,0,0,28,29,5,9,0,0,
        29,30,5,2,0,0,30,31,5,9,0,0,31,32,5,3,0,0,32,33,5,8,0,0,33,34,5,
        9,0,0,34,35,5,3,0,0,35,7,1,0,0,0,2,11,20
    ]

class TerceraParteParser ( Parser ):

    grammarFileName = "TerceraParte.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'encendido'", "'apagado'", 
                     "'mover'", "'rotar'", "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ENC", "APAG", "MOV", "ROT", "SUM", "INT", "NEWLINE", 
                      "WS" ]

    RULE_prog = 0
    RULE_dibujo = 1
    RULE_modo = 2
    RULE_puntero = 3

    ruleNames =  [ "prog", "dibujo", "modo", "puntero" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    ENC=4
    APAG=5
    MOV=6
    ROT=7
    SUM=8
    INT=9
    NEWLINE=10
    WS=11

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
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.dibujo()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1200) != 0)):
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


    class DibContext(DibujoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TerceraParteParser.DibujoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def puntero(self):
            return self.getTypedRuleContext(TerceraParteParser.PunteroContext,0)

        def NEWLINE(self):
            return self.getToken(TerceraParteParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDib" ):
                return visitor.visitDib(self)
            else:
                return visitor.visitChildren(self)



    def dibujo(self):

        localctx = TerceraParteParser.DibujoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_dibujo)
        try:
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5]:
                localctx = TerceraParteParser.ModContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.modo()
                self.state = 14
                self.match(TerceraParteParser.NEWLINE)
                pass
            elif token in [7]:
                localctx = TerceraParteParser.DibContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.puntero()
                self.state = 17
                self.match(TerceraParteParser.NEWLINE)
                pass
            elif token in [10]:
                localctx = TerceraParteParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 19
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
            self.state = 22
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


    class PunteroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TerceraParteParser.RULE_puntero

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PosContext(PunteroContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TerceraParteParser.PunteroContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ROT(self):
            return self.getToken(TerceraParteParser.ROT, 0)
        def MOV(self):
            return self.getToken(TerceraParteParser.MOV, 0)
        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(TerceraParteParser.INT)
            else:
                return self.getToken(TerceraParteParser.INT, i)
        def SUM(self):
            return self.getToken(TerceraParteParser.SUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPos" ):
                return visitor.visitPos(self)
            else:
                return visitor.visitChildren(self)



    def puntero(self):

        localctx = TerceraParteParser.PunteroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_puntero)
        try:
            localctx = TerceraParteParser.PosContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(TerceraParteParser.ROT)
            self.state = 25
            self.match(TerceraParteParser.T__0)
            self.state = 26
            self.match(TerceraParteParser.MOV)
            self.state = 27
            self.match(TerceraParteParser.T__0)
            self.state = 28
            self.match(TerceraParteParser.INT)
            self.state = 29
            self.match(TerceraParteParser.T__1)
            self.state = 30
            self.match(TerceraParteParser.INT)
            self.state = 31
            self.match(TerceraParteParser.T__2)
            self.state = 32
            self.match(TerceraParteParser.SUM)
            self.state = 33
            self.match(TerceraParteParser.INT)
            self.state = 34
            self.match(TerceraParteParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





