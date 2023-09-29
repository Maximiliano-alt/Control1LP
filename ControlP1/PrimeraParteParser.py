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
<<<<<<< HEAD
        4,1,10,37,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,21,8,1,1,2,1,2,1,3,1,3,1,3,
        1,3,1,3,3,3,30,8,3,1,3,1,3,1,3,3,3,35,8,3,1,3,0,0,4,0,2,4,6,0,2,
        1,0,4,5,1,0,6,7,37,0,9,1,0,0,0,2,20,1,0,0,0,4,22,1,0,0,0,6,34,1,
        0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,11,1,0,0,0,11,9,1,0,0,0,11,12,
        1,0,0,0,12,1,1,0,0,0,13,14,3,4,2,0,14,15,5,9,0,0,15,21,1,0,0,0,16,
        17,3,6,3,0,17,18,5,9,0,0,18,21,1,0,0,0,19,21,5,9,0,0,20,13,1,0,0,
        0,20,16,1,0,0,0,20,19,1,0,0,0,21,3,1,0,0,0,22,23,7,0,0,0,23,5,1,
        0,0,0,24,25,7,1,0,0,25,26,5,1,0,0,26,29,3,6,3,0,27,28,5,2,0,0,28,
        30,3,6,3,0,29,27,1,0,0,0,29,30,1,0,0,0,30,31,1,0,0,0,31,32,5,3,0,
        0,32,35,1,0,0,0,33,35,5,8,0,0,34,24,1,0,0,0,34,33,1,0,0,0,35,7,1,
        0,0,0,4,11,20,29,34
=======
        4,1,9,35,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,21,8,1,1,2,1,2,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,3,3,33,8,3,1,3,0,0,4,0,2,4,6,0,1,1,0,4,5,34,
        0,9,1,0,0,0,2,20,1,0,0,0,4,22,1,0,0,0,6,32,1,0,0,0,8,10,3,2,1,0,
        9,8,1,0,0,0,10,11,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,1,1,0,0,
        0,13,14,3,4,2,0,14,15,5,8,0,0,15,21,1,0,0,0,16,17,3,6,3,0,17,18,
        5,8,0,0,18,21,1,0,0,0,19,21,5,8,0,0,20,13,1,0,0,0,20,16,1,0,0,0,
        20,19,1,0,0,0,21,3,1,0,0,0,22,23,7,0,0,0,23,5,1,0,0,0,24,25,5,6,
        0,0,25,26,5,1,0,0,26,27,3,6,3,0,27,28,5,2,0,0,28,29,3,6,3,0,29,30,
        5,3,0,0,30,33,1,0,0,0,31,33,5,7,0,0,32,24,1,0,0,0,32,31,1,0,0,0,
        33,7,1,0,0,0,3,11,20,32
>>>>>>> 7483039019a702f260c0e1e044ebd4ebb7e8ccaf
    ]

class PrimeraParteParser ( Parser ):

    grammarFileName = "PrimeraParte.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'encendido'", "'apagado'", 
<<<<<<< HEAD
                     "'mover'", "'rotar'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ENC", "APAG", "MOV", "ROT", "INT", "NEWLINE", "WS" ]
=======
                     "'mover'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ENC", "APAG", "MOV", "INT", "NEWLINE", "WS" ]
>>>>>>> 7483039019a702f260c0e1e044ebd4ebb7e8ccaf

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
<<<<<<< HEAD
    ROT=7
    INT=8
    NEWLINE=9
    WS=10
=======
    INT=7
    NEWLINE=8
    WS=9
>>>>>>> 7483039019a702f260c0e1e044ebd4ebb7e8ccaf

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
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.dibujo()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
<<<<<<< HEAD
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1008) != 0)):
=======
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 496) != 0)):
>>>>>>> 7483039019a702f260c0e1e044ebd4ebb7e8ccaf
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



    class ModContext(DibujoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PrimeraParteParser.DibujoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def modo(self):
            return self.getTypedRuleContext(PrimeraParteParser.ModoContext,0)

        def NEWLINE(self):
            return self.getToken(PrimeraParteParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMod" ):
                return visitor.visitMod(self)
            else:
                return visitor.visitChildren(self)


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
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5]:
                localctx = PrimeraParteParser.ModContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.modo()
                self.state = 14
                self.match(PrimeraParteParser.NEWLINE)
                pass
<<<<<<< HEAD
            elif token in [6, 7, 8]:
=======
            elif token in [6, 7]:
>>>>>>> 7483039019a702f260c0e1e044ebd4ebb7e8ccaf
                localctx = PrimeraParteParser.DibContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.puntero()
                self.state = 17
                self.match(PrimeraParteParser.NEWLINE)
                pass
<<<<<<< HEAD
            elif token in [9]:
=======
            elif token in [8]:
>>>>>>> 7483039019a702f260c0e1e044ebd4ebb7e8ccaf
                localctx = PrimeraParteParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 19
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


    class ModoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PrimeraParteParser.RULE_modo

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AsignModContext(ModoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PrimeraParteParser.ModoContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def ENC(self):
            return self.getToken(PrimeraParteParser.ENC, 0)
        def APAG(self):
            return self.getToken(PrimeraParteParser.APAG, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignMod" ):
                return visitor.visitAsignMod(self)
            else:
                return visitor.visitChildren(self)



    def modo(self):

        localctx = PrimeraParteParser.ModoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_modo)
        self._la = 0 # Token type
        try:
            localctx = PrimeraParteParser.AsignModContext(self, localctx)
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
            return PrimeraParteParser.RULE_puntero

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PosContext(PunteroContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PrimeraParteParser.PunteroContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MOV(self):
            return self.getToken(PrimeraParteParser.MOV, 0)
        def puntero(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrimeraParteParser.PunteroContext)
            else:
                return self.getTypedRuleContext(PrimeraParteParser.PunteroContext,i)

<<<<<<< HEAD
        def MOV(self):
            return self.getToken(PrimeraParteParser.MOV, 0)
        def ROT(self):
            return self.getToken(PrimeraParteParser.ROT, 0)
=======
>>>>>>> 7483039019a702f260c0e1e044ebd4ebb7e8ccaf

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
        self.enterRule(localctx, 6, self.RULE_puntero)
<<<<<<< HEAD
        self._la = 0 # Token type
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7]:
                localctx = PrimeraParteParser.PosContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
=======
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = PrimeraParteParser.PosContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.match(PrimeraParteParser.MOV)
>>>>>>> 7483039019a702f260c0e1e044ebd4ebb7e8ccaf
                self.state = 25
                self.match(PrimeraParteParser.T__0)
                self.state = 26
                self.puntero()
<<<<<<< HEAD
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 27
                    self.match(PrimeraParteParser.T__1)
                    self.state = 28
                    self.puntero()


                self.state = 31
                self.match(PrimeraParteParser.T__2)
                pass
            elif token in [8]:
                localctx = PrimeraParteParser.INTContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 33
=======
                self.state = 27
                self.match(PrimeraParteParser.T__1)
                self.state = 28
                self.puntero()
                self.state = 29
                self.match(PrimeraParteParser.T__2)
                pass
            elif token in [7]:
                localctx = PrimeraParteParser.INTContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 31
>>>>>>> 7483039019a702f260c0e1e044ebd4ebb7e8ccaf
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





