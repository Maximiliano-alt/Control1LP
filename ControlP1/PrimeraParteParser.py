# Generated from PrimeraParte.g4 by ANTLR 4.13.1
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
        4,1,8,28,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,1,1,
        1,1,1,1,1,3,1,16,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,26,8,2,
        1,2,0,0,3,0,2,4,0,1,1,0,4,5,27,0,7,1,0,0,0,2,15,1,0,0,0,4,25,1,0,
        0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,
        10,1,1,0,0,0,11,12,3,4,2,0,12,13,5,7,0,0,13,16,1,0,0,0,14,16,5,7,
        0,0,15,11,1,0,0,0,15,14,1,0,0,0,16,3,1,0,0,0,17,18,5,1,0,0,18,19,
        3,4,2,0,19,20,5,2,0,0,20,21,3,4,2,0,21,22,5,3,0,0,22,23,7,0,0,0,
        23,26,1,0,0,0,24,26,5,6,0,0,25,17,1,0,0,0,25,24,1,0,0,0,26,5,1,0,
        0,0,3,9,15,25
    ]

class PrimeraParteParser ( Parser ):

    grammarFileName = "PrimeraParte.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'encendido'", "'apagado'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ENC", "APAG", "INT", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_dibujo = 1
    RULE_puntero = 2

    ruleNames =  [ "prog", "dibujo", "puntero" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    ENC=4
    APAG=5
    INT=6
    NEWLINE=7
    WS=8

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
                return self.getTypedRuleContexts(PrimeraParteParser.DibujoContext)
            else:
                return self.getTypedRuleContext(PrimeraParteParser.DibujoContext,i)


        def getRuleIndex(self):
            return PrimeraParteParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = PrimeraParteParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.dibujo()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 194) != 0)):
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
            return PrimeraParteParser.RULE_dibujo

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(DibujoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PrimeraParteParser.DibujoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(PrimeraParteParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class DibContext(DibujoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PrimeraParteParser.DibujoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def puntero(self):
            return self.getTypedRuleContext(PrimeraParteParser.PunteroContext,0)

        def NEWLINE(self):
            return self.getToken(PrimeraParteParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDib" ):
                return visitor.visitDib(self)
            else:
                return visitor.visitChildren(self)



    def dibujo(self):

        localctx = PrimeraParteParser.DibujoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_dibujo)
        try:
            self.state = 15
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 6]:
                localctx = PrimeraParteParser.DibContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.puntero()
                self.state = 12
                self.match(PrimeraParteParser.NEWLINE)
                pass
            elif token in [7]:
                localctx = PrimeraParteParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(PrimeraParteParser.NEWLINE)
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


    class PunteroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PrimeraParteParser.RULE_puntero

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PosContext(PunteroContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PrimeraParteParser.PunteroContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def puntero(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrimeraParteParser.PunteroContext)
            else:
                return self.getTypedRuleContext(PrimeraParteParser.PunteroContext,i)

        def ENC(self):
            return self.getToken(PrimeraParteParser.ENC, 0)
        def APAG(self):
            return self.getToken(PrimeraParteParser.APAG, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPos" ):
                return visitor.visitPos(self)
            else:
                return visitor.visitChildren(self)


    class INTContext(PunteroContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PrimeraParteParser.PunteroContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(PrimeraParteParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitINT" ):
                return visitor.visitINT(self)
            else:
                return visitor.visitChildren(self)



    def puntero(self):

        localctx = PrimeraParteParser.PunteroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_puntero)
        self._la = 0 # Token type
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = PrimeraParteParser.PosContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.match(PrimeraParteParser.T__0)
                self.state = 18
                self.puntero()
                self.state = 19
                self.match(PrimeraParteParser.T__1)
                self.state = 20
                self.puntero()
                self.state = 21
                self.match(PrimeraParteParser.T__2)
                self.state = 22
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==4 or _la==5):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [6]:
                localctx = PrimeraParteParser.INTContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.match(PrimeraParteParser.INT)
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





