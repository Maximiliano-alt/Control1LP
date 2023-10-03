# Generated from SegundaParte.g4 by ANTLR 4.13.1
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
        4,1,10,43,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,21,8,1,1,2,1,2,1,3,1,3,1,3,
        1,3,1,3,3,3,30,8,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,38,8,3,1,3,3,3,41,
        8,3,1,3,0,0,4,0,2,4,6,0,1,1,0,4,5,44,0,9,1,0,0,0,2,20,1,0,0,0,4,
        22,1,0,0,0,6,40,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,11,1,0,0,0,11,
        9,1,0,0,0,11,12,1,0,0,0,12,1,1,0,0,0,13,14,3,4,2,0,14,15,5,9,0,0,
        15,21,1,0,0,0,16,17,3,6,3,0,17,18,5,9,0,0,18,21,1,0,0,0,19,21,5,
        9,0,0,20,13,1,0,0,0,20,16,1,0,0,0,20,19,1,0,0,0,21,3,1,0,0,0,22,
        23,7,0,0,0,23,5,1,0,0,0,24,25,5,6,0,0,25,26,5,1,0,0,26,29,5,8,0,
        0,27,28,5,2,0,0,28,30,5,8,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,31,
        1,0,0,0,31,41,5,3,0,0,32,33,5,7,0,0,33,34,5,1,0,0,34,37,5,8,0,0,
        35,36,5,2,0,0,36,38,5,8,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,39,1,
        0,0,0,39,41,5,3,0,0,40,24,1,0,0,0,40,32,1,0,0,0,41,7,1,0,0,0,5,11,
        20,29,37,40
    ]

class SegundaParteParser ( Parser ):

    grammarFileName = "SegundaParte.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'encendido'", "'apagado'", 
                     "'mover'", "'rotar'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ENC", "APAG", "MOV", "ROT", "INT", "NEWLINE", "WS" ]

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
    INT=8
    NEWLINE=9
    WS=10

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
                return self.getTypedRuleContexts(SegundaParteParser.DibujoContext)
            else:
                return self.getTypedRuleContext(SegundaParteParser.DibujoContext,i)


        def getRuleIndex(self):
            return SegundaParteParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = SegundaParteParser.ProgContext(self, self._ctx, self.state)
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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 752) != 0)):
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
            return SegundaParteParser.RULE_dibujo

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ModContext(DibujoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SegundaParteParser.DibujoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def modo(self):
            return self.getTypedRuleContext(SegundaParteParser.ModoContext,0)

        def NEWLINE(self):
            return self.getToken(SegundaParteParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMod" ):
                return visitor.visitMod(self)
            else:
                return visitor.visitChildren(self)


    class BlankContext(DibujoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SegundaParteParser.DibujoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(SegundaParteParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class DibContext(DibujoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SegundaParteParser.DibujoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def puntero(self):
            return self.getTypedRuleContext(SegundaParteParser.PunteroContext,0)

        def NEWLINE(self):
            return self.getToken(SegundaParteParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDib" ):
                return visitor.visitDib(self)
            else:
                return visitor.visitChildren(self)



    def dibujo(self):

        localctx = SegundaParteParser.DibujoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_dibujo)
        try:
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5]:
                localctx = SegundaParteParser.ModContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.modo()
                self.state = 14
                self.match(SegundaParteParser.NEWLINE)
                pass
            elif token in [6, 7]:
                localctx = SegundaParteParser.DibContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.puntero()
                self.state = 17
                self.match(SegundaParteParser.NEWLINE)
                pass
            elif token in [9]:
                localctx = SegundaParteParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 19
                self.match(SegundaParteParser.NEWLINE)
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
            return SegundaParteParser.RULE_modo

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AsignModContext(ModoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SegundaParteParser.ModoContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def ENC(self):
            return self.getToken(SegundaParteParser.ENC, 0)
        def APAG(self):
            return self.getToken(SegundaParteParser.APAG, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignMod" ):
                return visitor.visitAsignMod(self)
            else:
                return visitor.visitChildren(self)



    def modo(self):

        localctx = SegundaParteParser.ModoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_modo)
        self._la = 0 # Token type
        try:
            localctx = SegundaParteParser.AsignModContext(self, localctx)
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
            return SegundaParteParser.RULE_puntero

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MovContext(PunteroContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SegundaParteParser.PunteroContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MOV(self):
            return self.getToken(SegundaParteParser.MOV, 0)
        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(SegundaParteParser.INT)
            else:
                return self.getToken(SegundaParteParser.INT, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMov" ):
                return visitor.visitMov(self)
            else:
                return visitor.visitChildren(self)


    class RotContext(PunteroContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SegundaParteParser.PunteroContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ROT(self):
            return self.getToken(SegundaParteParser.ROT, 0)
        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(SegundaParteParser.INT)
            else:
                return self.getToken(SegundaParteParser.INT, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRot" ):
                return visitor.visitRot(self)
            else:
                return visitor.visitChildren(self)



    def puntero(self):

        localctx = SegundaParteParser.PunteroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_puntero)
        self._la = 0 # Token type
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = SegundaParteParser.MovContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.match(SegundaParteParser.MOV)
                self.state = 25
                self.match(SegundaParteParser.T__0)
                self.state = 26
                self.match(SegundaParteParser.INT)
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 27
                    self.match(SegundaParteParser.T__1)
                    self.state = 28
                    self.match(SegundaParteParser.INT)


                self.state = 31
                self.match(SegundaParteParser.T__2)
                pass
            elif token in [7]:
                localctx = SegundaParteParser.RotContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.match(SegundaParteParser.ROT)
                self.state = 33
                self.match(SegundaParteParser.T__0)
                self.state = 34
                self.match(SegundaParteParser.INT)
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 35
                    self.match(SegundaParteParser.T__1)
                    self.state = 36
                    self.match(SegundaParteParser.INT)


                self.state = 39
                self.match(SegundaParteParser.T__2)
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





